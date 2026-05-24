##Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set(style="whitegrid")

##Load Cleaned Dataset
df = pd.read_csv("cleaned_hotel_bookings.csv")
df.head()


##Basic Dataset Information
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())
df.info()
df.describe()


##Check Missing Values
missing_values = df.isnull().sum().sort_values(ascending=False)
missing_values[missing_values > 0]

## Overall Cancellation Analysis
##Overall Cancellation Count
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="booking_status")
plt.title("Overall Booking Cancellation Status")
plt.xlabel("Booking Status")
plt.ylabel("Number of Bookings")
plt.show()


##Cancellation Rate
cancellation_rate = df["is_canceled"].mean() * 100
print(f"Overall Cancellation Rate: {cancellation_rate:.2f}%") 

##Cancellation Rate by Hotel Type
hotel_cancel_rate = df.groupby("hotel")["is_canceled"].mean().reset_index()
hotel_cancel_rate["cancellation_rate"] = hotel_cancel_rate["is_canceled"] * 100
hotel_cancel_rate
plt.figure(figsize=(7, 5))
sns.barplot(data=hotel_cancel_rate, x="hotel", y="cancellation_rate")
plt.title("Cancellation Rate by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Cancellation Rate (%)")
plt.show()


##Dynamic Pricing Analysis Using ADR
## Average Daily Rate by Hotel Type
adr_by_hotel = df.groupby("hotel")["adr"].mean().reset_index()
adr_by_hotel
plt.figure(figsize=(7, 5))
sns.barplot(data=adr_by_hotel, x="hotel", y="adr")
plt.title("Average Daily Rate by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Average Daily Rate")
plt.show()

##Average Daily Rate by Month
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

adr_by_month = df.groupby("arrival_date_month")["adr"].mean().reindex(month_order).reset_index()
adr_by_month
plt.figure(figsize=(12, 5))
sns.lineplot(data=adr_by_month, x="arrival_date_month", y="adr", marker="o")
plt.title("Average Daily Rate by Month")
plt.xlabel("Month")
plt.ylabel("Average Daily Rate")
plt.xticks(rotation=45)
plt.show()


##ADR by Season
season_order = ["Winter", "Spring", "Summer", "Autumn"]
adr_by_season = df.groupby("season")["adr"].mean().reindex(season_order).reset_index()
adr_by_season
plt.figure(figsize=(8, 5))
sns.barplot(data=adr_by_season, x="season", y="adr", order=season_order)
plt.title("Average Daily Rate by Season")
plt.xlabel("Season")
plt.ylabel("Average Daily Rate")
plt.show()


##ADR Distribution
plt.figure(figsize=(10, 5))
sns.histplot(df["adr"], bins=50, kde=True)
plt.title("Distribution of Average Daily Rate")
plt.xlabel("Average Daily Rate")
plt.ylabel("Frequency")
plt.show()


##ADR by Cancellation Status
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="booking_status", y="adr")
plt.title("ADR Distribution by Booking Status")
plt.xlabel("Booking Status")
plt.ylabel("Average Daily Rate")
plt.show()

##Seasonal Demand Analysis
## Booking Volume by Month
booking_volume_month = df["arrival_date_month"].value_counts().reindex(month_order).reset_index()
booking_volume_month.columns = ["arrival_date_month", "booking_count"]
booking_volume_month
plt.figure(figsize=(12, 5))
sns.barplot(data=booking_volume_month, x="arrival_date_month", y="booking_count")
plt.title("Booking Volume by Month")
plt.xlabel("Month")
plt.ylabel("Number of Bookings")
plt.xticks(rotation=45)
plt.show()


##Booking Volume by Season
booking_volume_season = df["season"].value_counts().reindex(season_order).reset_index()
booking_volume_season.columns = ["season", "booking_count"]
booking_volume_season
plt.figure(figsize=(8, 5))
sns.barplot(data=booking_volume_season, x="season", y="booking_count", order=season_order)
plt.title("Booking Volume by Season")
plt.xlabel("Season")
plt.ylabel("Number of Bookings")
plt.show()


##Monthly ADR vs Booking Volume
monthly_summary = df.groupby("arrival_date_month").agg(
    average_adr=("adr", "mean"),
    booking_count=("hotel", "count"),
    cancellation_rate=("is_canceled", "mean")
).reindex(month_order).reset_index()
monthly_summary["cancellation_rate"] = monthly_summary["cancellation_rate"] * 100
monthly_summary
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_summary, x="arrival_date_month", y="average_adr", marker="o", label="Average ADR")
plt.title("Monthly Average ADR Trend")
plt.xlabel("Month")
plt.ylabel("Average ADR")
plt.xticks(rotation=45)
plt.show()
plt.figure(figsize=(12, 5))
sns.lineplot(data=monthly_summary, x="arrival_date_month", y="booking_count", marker="o", label="Booking Count")
plt.title("Monthly Booking Demand Trend")
plt.xlabel("Month")
plt.ylabel("Booking Count")
plt.xticks(rotation=45)
plt.show()


##Customer Retention and Cancellation Drivers
##Cancellation by Lead Time Category
lead_cancel = pd.crosstab(
    df["lead_time_category"],
    df["booking_status"],
    normalize="index"
) * 100
lead_cancel
lead_cancel.plot(kind="bar", figsize=(10, 5))
plt.title("Cancellation Percentage by Lead Time Category")
plt.xlabel("Lead Time Category")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend(title="Booking Status")
plt.show()


##Cancellation by Market Segment
market_cancel = pd.crosstab(
    df["market_segment"],
    df["booking_status"],
    normalize="index"
) * 100
market_cancel
market_cancel.plot(kind="bar", figsize=(12, 5))
plt.title("Cancellation Percentage by Market Segment")
plt.xlabel("Market Segment")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend(title="Booking Status")
plt.show()


## Cancellation by Deposit Type
deposit_cancel = pd.crosstab(
    df["deposit_type"],
    df["booking_status"],
    normalize="index"
) * 100
deposit_cancel
deposit_cancel.plot(kind="bar", figsize=(8, 5))
plt.title("Cancellation Percentage by Deposit Type")
plt.xlabel("Deposit Type")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend(title="Booking Status")
plt.show()


##Cancellation by Customer Type
customer_cancel = pd.crosstab(
    df["customer_type"],
    df["booking_status"],
    normalize="index"
) * 100
customer_cancel
customer_cancel.plot(kind="bar", figsize=(10, 5))
plt.title("Cancellation Percentage by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend(title="Booking Status")
plt.show()


##Revenue Analysis
##Total Estimated Revenue
total_revenue = df["estimated_revenue"].sum()
print(f"Total Estimated Revenue: {total_revenue:,.2f}")
## Revenue by Hotel Type
revenue_by_hotel = df.groupby("hotel")["estimated_revenue"].sum().reset_index()
revenue_by_hotel
plt.figure(figsize=(7, 5))
sns.barplot(data=revenue_by_hotel, x="hotel", y="estimated_revenue")
plt.title("Estimated Revenue by Hotel Type")
plt.xlabel("Hotel Type")
plt.ylabel("Estimated Revenue")
plt.show()


##Revenue by Month
revenue_by_month = df.groupby("arrival_date_month")["estimated_revenue"].sum().reindex(month_order).reset_index()
revenue_by_month
plt.figure(figsize=(12, 5))
sns.lineplot(data=revenue_by_month, x="arrival_date_month", y="estimated_revenue", marker="o")
plt.title("Estimated Revenue by Month")
plt.xlabel("Month")
plt.ylabel("Estimated Revenue")
plt.xticks(rotation=45)
plt.show()



##Revenue by Customer Type
revenue_by_customer = df.groupby("customer_type")["estimated_revenue"].sum().reset_index()
revenue_by_customer
plt.figure(figsize=(10, 5))
sns.barplot(data=revenue_by_customer, x="customer_type", y="estimated_revenue")
plt.title("Estimated Revenue by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Estimated Revenue")
plt.xticks(rotation=45)
plt.show()



##Correlation Analysis
## Correlation Matrix
numeric_columns = [
    "is_canceled",
    "lead_time",
    "arrival_date_year",
    "arrival_date_week_number",
    "arrival_date_day_of_month",
    "stays_in_weekend_nights",
    "stays_in_week_nights",
    "adults",
    "children",
    "babies",
    "is_repeated_guest",
    "previous_cancellations",
    "previous_bookings_not_canceled",
    "booking_changes",
    "days_in_waiting_list",
    "adr",
    "required_car_parking_spaces",
    "total_of_special_requests",
    "total_stay",
    "total_guests",
    "estimated_revenue"
]
corr = df[numeric_columns].corr()
plt.figure(figsize=(16, 10))
sns.heatmap(corr, annot=False, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()


##Correlation with Cancellation
cancel_corr = corr["is_canceled"].sort_values(ascending=False)
cancel_corr
plt.figure(figsize=(8, 8))
cancel_corr.drop("is_canceled").plot(kind="barh")
plt.title("Correlation of Features with Cancellation")
plt.xlabel("Correlation")
plt.ylabel("Features")
plt.show()


##Customer Segmentation
## Segment Customers by Booking Behavior
def customer_segment(row):
    if row["is_repeated_guest"] == 1:
        return "Repeated Guest"
    elif row["lead_time"] <= 7:
        return "Last-Minute Booker"
    elif row["lead_time"] > 90:
        return "Early Planner"
    elif row["market_segment"] in ["Corporate"]:
        return "Corporate Customer"
    else:
        return "Regular Customer"
df["customer_segment"] = df.apply(customer_segment, axis=1)
df["customer_segment"].value_counts()


## Cancellation by Customer Segment
segment_cancel = pd.crosstab(
    df["customer_segment"],
    df["booking_status"],
    normalize="index"
) * 100
segment_cancel
segment_cancel.plot(kind="bar", figsize=(12, 5))
plt.title("Cancellation Percentage by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Percentage")
plt.xticks(rotation=45)
plt.legend(title="Booking Status")
plt.show()



## Revenue by Customer Segment
segment_revenue = df.groupby("customer_segment")["estimated_revenue"].sum().reset_index()
segment_revenue
plt.figure(figsize=(12, 5))
sns.barplot(data=segment_revenue, x="customer_segment", y="estimated_revenue")
plt.title("Estimated Revenue by Customer Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Estimated Revenue")
plt.xticks(rotation=45)
plt.show()



##Business Insights Summary
## Generate Key Business Metrics
total_bookings = len(df)
total_cancellations = df["is_canceled"].sum()
cancellation_rate = total_cancellations / total_bookings * 100
average_adr = df["adr"].mean()
total_revenue = df["estimated_revenue"].sum()
highest_adr_month = monthly_summary.loc[monthly_summary["average_adr"].idxmax(), "arrival_date_month"]
highest_booking_month = monthly_summary.loc[monthly_summary["booking_count"].idxmax(), "arrival_date_month"]
highest_cancel_month = monthly_summary.loc[monthly_summary["cancellation_rate"].idxmax(), "arrival_date_month"]
print("Business Summary")
print("----------------")
print(f"Total Bookings: {total_bookings:,}")
print(f"Total Cancellations: {total_cancellations:,}")
print(f"Cancellation Rate: {cancellation_rate:.2f}%")
print(f"Average ADR: {average_adr:.2f}")
print(f"Total Estimated Revenue: {total_revenue:,.2f}")
print(f"Highest ADR Month: {highest_adr_month}")
print(f"Highest Booking Demand Month: {highest_booking_month}")
print(f"Highest Cancellation Rate Month: {highest_cancel_month}")


##Save EDA Output Dataset for Dashboard
df.to_csv("eda_hotel_bookings.csv", index=False)
print("EDA dataset saved successfully.")
## Final EDA Insights
















