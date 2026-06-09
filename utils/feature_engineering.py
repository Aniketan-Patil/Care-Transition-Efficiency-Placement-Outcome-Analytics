import numpy as np


def create_features(df):

    # Calendar Features
    df["Year"] = df["Date"].dt.year

    df["Month"] = df["Date"].dt.month

    df["Quarter"] = df["Date"].dt.quarter

    df["Weekday"] = df["Date"].dt.day_name()

    df["DayOfWeek"] = df["Date"].dt.dayofweek

    df["WeekOfYear"] = df["Date"].dt.isocalendar().week

    # Weekend Flag
    df["Is_Weekend"] = np.where(
        df["DayOfWeek"] >= 5,
        1,
        0
    )

    df["Sudden_Drop"] = (
    df["HHS_Discharged"].pct_change()
    ) * 100
    
    return df

    