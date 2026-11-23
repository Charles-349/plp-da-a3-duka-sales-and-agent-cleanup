
import pandas as pd


def clean_agent_data(txns, agents):
    """
    Clean agent transaction data and return a cleaning log.

    Handles:
    - Duplicate transaction IDs
    - Inconsistent transaction types
    - Missing and invalid amounts
    - Date format inconsistencies
    - IQR outlier detection
    - Unknown agent references

    Returns:
        clean_df: Cleaned transaction DataFrame.
        log: Dictionary containing cleaning statistics.
    """

    clean_df = txns.copy()
    agents_df = agents.copy()

    original_rows = len(clean_df)

    # 1. Audit duplicates before removing them
    exact_duplicates = int(clean_df.duplicated().sum())
    duplicate_ids = int(clean_df["txn_id"].duplicated().sum())

    # Keep the first occurrence of each transaction ID
    clean_df = clean_df.drop_duplicates(
        subset=["txn_id"],
        keep="first"
    ).copy()

    # 2. Standardize transaction types
    clean_df["txn_type"] = (
        clean_df["txn_type"]
        .astype("string")
        .str.strip()
        .str.title()
    )

    # 3. Convert amounts to numeric
    clean_df["amount"] = pd.to_numeric(
        clean_df["amount"],
        errors="coerce"
    )

    # Flag missing or invalid amounts
    clean_df["amount_missing"] = clean_df["amount"].isna()

    # Missing financial values are retained as NaN.
    # No artificial transaction amounts are created.

    # 4. Standardize transaction dates
    clean_df["txn_date"] = (
        clean_df["txn_date"]
        .astype("string")
        .str.replace("/", "-", regex=False)
    )

    clean_df["txn_date"] = pd.to_datetime(
        clean_df["txn_date"],
        errors="coerce"
    )

    # 5. Detect outliers using the IQR method
    valid_amounts = clean_df["amount"].dropna()

    if len(valid_amounts) > 0:
        q1 = valid_amounts.quantile(0.25)
        q3 = valid_amounts.quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        clean_df["amount_outlier"] = (
            (clean_df["amount"] < lower_bound) |
            (clean_df["amount"] > upper_bound)
        )
    else:
        clean_df["amount_outlier"] = False

    # 6. Merge agent details, retaining unknown agents
    clean_df = clean_df.merge(
        agents_df,
        on="agent_id",
        how="left",
        validate="many_to_one",
        indicator=True
    )

    unknown_agents = int(
        (clean_df["_merge"] == "left_only").sum()
    )

    clean_df["county"] = clean_df["county"].fillna("Unknown")

    clean_df = clean_df.drop(columns=["_merge"])

    # 7. Create cleaning log
    log = {
        "original_rows": original_rows,
        "exact_duplicate_rows": exact_duplicates,
        "duplicate_ids_removed": duplicate_ids,
        "final_rows": len(clean_df),
        "missing_amounts": int(clean_df["amount_missing"].sum()),
        "outliers_flagged": int(clean_df["amount_outlier"].sum()),
        "unknown_agent_transactions": unknown_agents,
        "invalid_dates": int(clean_df["txn_date"].isna().sum())
    }

    return clean_df, log
