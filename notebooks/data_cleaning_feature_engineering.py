import pandas as pd
import numpy as np
df = pd.read_csv("hotel_bookings.csv")
df.head()
df.shape
df.info()
df.isnull().sum()
df["children"] = df["children"].fillna(0)
df["country"] = df["country"].fillna("Unknown")
df["agent"] = df["agent"].fillna(0)
df["company"] = df["company"].fillna(0)

df = df.drop_duplicates()

##Feature engineering code
df["booking_status"] = df["is_canceled"].map({
    0: "Not Canceled",
    1: "Canceled"
})

df["total_stay"] = df["stays_in_weekend_nights"] + df["stays_in_week_nights"]

df["total_guests"] = df["adults"] + df["children"] + df["babies"]

df["lead_time_category"] = pd.cut(
    df["lead_time"],
    bins=[-1, 7, 30, 90, df["lead_time"].max()],
    labels=["Last-Minute", "Short-Term", "Medium-Term", "Long-Term"]
)

def get_season(month):
    if month in ["December", "January", "February"]:
        return "Winter"
    elif month in ["March", "April", "May"]:
        return "Spring"
    elif month in ["June", "July", "August"]:
        return "Summer"
    else:
        return "Autumn"

df["season"] = df["arrival_date_month"].apply(get_season)

df["estimated_revenue"] = np.where(
    df["is_canceled"] == 0,
    df["adr"] * df["total_stay"],
    0
)
##Remove invalid records using Python
df = df[df["total_guests"] > 0]
df = df[df["adr"] >= 0]
df = df[df["adr"] <= 1000]
df = df[df["total_stay"] > 0]

##Save cleaned data
df.to_csv("cleaned_hotel_bookings.csv", index=False)
