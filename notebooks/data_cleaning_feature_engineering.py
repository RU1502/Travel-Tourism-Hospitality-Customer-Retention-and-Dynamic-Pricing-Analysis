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
