# PLP Data Analysis – Assignment 3

This repository contains two data analysis projects completed as part of PLP Data Analysis Assignment 3.

## Project 1: Duka Electronics Sales Exploration

**Reporting period:** January – June 2026

### Objectives
- Analyse sales performance across five branches.
- Identify revenue trends.
- Evaluate product performance.
- Compare weekday and weekend sales.
- Identify premium online sales opportunities.

### Key Findings
- Total revenue: **KES 71,792,500** from 1,000 orders.
- Nairobi was the best-performing branch, generating KES 26,106,100.
- Laptops generated the highest product revenue at KES 41,535,000.
- Tablets recorded the highest sales volume at 691 units.
- April was the best-performing month, generating KES 13,518,300.
- The premium online filter identified 83 orders worth KES 10,218,000.

### Deliverables
- `generate_data.py` – Generates the sales dataset.
- `duka_sales_exploration.ipynb` – Exploratory analysis and business insights.
- `excel/duka_branch_summary.xlsx` – Excel workbook containing sales data, formula-driven branch summaries using SUMIFS and XLOOKUP, and a native PivotTable.
- `outputs/premium_online_coast_capital.csv` – Filtered premium online sales for Nairobi and Mombasa.

## Project 2: Agent Transaction Data Cleaning

### Objectives
- Audit transaction data quality.
- Identify and remove duplicate transaction IDs.
- Standardize transaction types and dates.
- Handle missing and invalid financial values.
- Detect potential outliers.
- Validate agent references.
- Produce county and weekly transaction summaries.

### Cleaning Results

| Metric | Result |
|---|---:|
| Original records | 612 |
| Final records | 600 |
| Duplicate transaction IDs remaining | 0 |
| Missing transaction amounts | 20 |
| Invalid transaction dates | 0 |
| Unknown agent transactions | 7 |
| Potential IQR outliers flagged | 40 |

### Cleaning Decisions
- Duplicate transaction IDs were resolved by retaining the first occurrence.
- Missing amounts were retained rather than replaced with invented values.
- Potential outliers were flagged for investigation rather than automatically deleted.
- Unknown agent references were retained and assigned the county `Unknown`.
- Transaction types were standardized to Deposit and Withdrawal.

### Deliverables
- `agent_cleanup.ipynb` – Data quality audit, cleaning, analysis and reporting.
- `cleaning_pipeline.py` – Reusable transaction cleaning function.
- `outputs/agent_transactions_clean.csv` – Cleaned transaction dataset.

## Technologies Used

- Python
- Pandas
- NumPy
- Google Colab / Jupyter Notebook
- Microsoft Excel
- OpenPyXL

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## Running the Projects

### Duka Electronics

Generate the sales dataset:

```bash
python generate_data.py
```

Open `duka_sales_exploration.ipynb` in Google Colab or Jupyter Notebook and execute the cells in order.

### Agent Transaction Cleaning

Open `agent_cleanup.ipynb` in Google Colab or Jupyter Notebook and execute all cells in order.

The notebook automatically generates the sample agent and transaction datasets using a fixed random seed, creates the reusable `cleaning_pipeline.py` module, performs the cleaning and analysis, and exports the cleaned transaction CSV.

## Data Integrity and Privacy

Financial records were preserved during cleaning. Missing values, potential outliers and unknown agent references were documented for further investigation.

Raw input CSV files have been excluded from the repository. Transaction and agent information should be handled securely and shared only with authorized personnel.

## Conclusion

Both projects demonstrate practical data analysis and data quality management skills, from generating datasets and exploring business performance to developing reusable cleaning functions and producing structured analytical reports.
