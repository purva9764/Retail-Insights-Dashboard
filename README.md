# Retail Insights – Sales Analytics Dashboard

## Project Overview
Retail Insights is a Python-based Data Analytics project developed using Streamlit. It helps users explore and analyse retail sales data through interactive dashboards, visualisations, filters, and key performance indicators (KPIs).

## Project Objectives
- Analyse retail sales and profit.
- Identify top-performing products and categories.
- Understand monthly sales trends.
- Compare sales and profit across different regions.
- Perform basic data cleaning and data quality checks.

## Technologies Used
- Python
- Pandas
- Matplotlib
- Seaborn
- Plotly
- Streamlit

## Project Features
- Interactive sales dashboard.
- Total sales, profit, orders, and average order value.
- Category-wise sales analysis.
- Monthly sales trend visualisation.
- Region-wise profit analysis.
- Product performance analysis.
- Dataset preview.
- Data cleaning and data quality report.
- Download cleaned dataset as a CSV file.

## Project Structure

```text
Retail_Sales_Data_Analysis/
│
├── app.py
├── main.py
├── generate_data.py
├── requirements.txt
├── README.md
│
└── data/
    └── retail_sales.csv
```

## Dataset Information
This project uses a simulated retail sales dataset containing 250 records. The dataset was generated for learning and demonstration purposes. It does not represent actual company transactions.

The dataset includes information such as:
- Order ID
- Order Date
- Product
- Category
- Region
- Sales
- Profit

## Data Cleaning
The project uses Pandas to perform basic data cleaning operations:
- Checking missing values.
- Removing duplicate records.
- Converting columns into appropriate data types.
- Preparing cleaned data for analysis.

## How to Run the Project

1. Install Python.
2. Open the project folder in VS Code.
3. Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
python -m streamlit run app.py
```

5. Open the local URL displayed in the terminal to view the dashboard.

## Learning Outcomes
- Loading and exploring datasets using Pandas.
- Data cleaning and preprocessing.
- Grouping and summarising data.
- Analysing sales and profit.
- Creating interactive visualisations.
- Developing a dashboard using Streamlit.

## Project Purpose
This project was developed as a practical learning project to demonstrate Python programming and data analytics skills.

## Author
Python & Data Analytics Internship Project