# Hotel Booking Customer Retention and Dynamic Pricing Analysis

## Project Title

**Travel, Tourism & Hospitality: Customer Retention and Dynamic Pricing Analysis**

## Project Overview

This project analyzes historical hotel booking data to identify customer cancellation patterns, understand seasonal pricing behavior, segment customers based on booking behavior, and build a baseline machine learning model to predict booking cancellations.

The project is designed as part of the Data Analytics internship project requirement for the Travel, Tourism & Hospitality domain. The main objective is to support hotel revenue managers and marketing teams in reducing cancellation risk, improving customer retention, and applying data-driven dynamic pricing strategies.

## Business Problem

Hotels and travel businesses often face revenue loss due to unexpected booking cancellations and unoptimized room pricing. Traditional booking systems may not provide enough insight into why customers cancel, which customer groups are risky, or how prices change with demand and seasonality.

This project solves the problem by analyzing hotel booking data and answering key business questions:

- What is the overall cancellation rate?
- Which hotel type has more cancellations?
- Which market segments cancel more frequently?
- How does lead time affect cancellation behavior?
- How does Average Daily Rate vary by month and season?
- Which customer segments generate higher revenue?
- Can we predict whether a booking will be cancelled?

## Dataset

The dataset used in this project is the **Hotel Booking Demand Dataset**.

The dataset contains hotel booking records with information such as:

- Hotel type
- Cancellation status
- Lead time
- Arrival year and month
- Length of stay
- Number of guests
- Meal type
- Country
- Market segment
- Distribution channel
- Repeated guest status
- Deposit type
- Customer type
- Average Daily Rate
- Reservation status

## Tools and Technologies Used

| Category | Tools / Technologies |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| Data Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-Learn |
| Database | MySQL, MySQL Workbench |
| Dashboard | Power BI |
| Development Environment | Jupyter Notebook |
| Version Control | Git, GitHub |

## Project Workflow

The project follows an end-to-end data analytics workflow:

1. Data collection
2. Data cleaning
3. Feature engineering
4. Exploratory Data Analysis
5. Dynamic pricing analysis
6. Customer segmentation
7. SQL-based business analysis
8. Cancellation prediction modeling
9. Power BI dashboard creation
10. Business insights and recommendations

## Project Folder Structure

```text
hotel-booking-retention-analysis/
│
├── data/
│   ├── hotel_bookings.csv
│   ├── cleaned_hotel_bookings.csv
│   ├── eda_hotel_bookings.csv
│   ├── model_comparison_results.csv
│   └── feature_importance_results.csv
│
├── notebooks/
│   ├── 01_data_cleaning_feature_engineering.ipynb
│   ├── 02_eda_dynamic_pricing_analysis.ipynb
│   └── 03_cancellation_prediction_model.ipynb
│
├── sql/
│   └── booking_analysis_queries.sql
│
├── dashboard/
│   ├── Hotel_Management_Dashboard.pbix
│   └── dashboard_screenshot.png
│
├── reports/
│   └── final_project_report.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
