import pandas as pd
import numpy as np


def load_and_clean_data():

    df = pd.read_csv(
        "data/HHS_Unaccompanied_Alien_Children_Program.csv"
    )

    # Remove empty rows
    df = df.dropna(how="all")

    # Rename columns
    df.columns = [
        "Date",
        "CBP_Apprehended",
        "CBP_Custody",
        "CBP_Transferred",
        "HHS_Care",
        "HHS_Discharged"
    ]

    # Convert date
    df["Date"] = pd.to_datetime(df["Date"])

    # Remove commas
    df["HHS_Care"] = (
        df["HHS_Care"]
        .astype(str)
        .str.replace(",", "")
    )

    # Numeric conversion
    numeric_cols = [
        "CBP_Apprehended",
        "CBP_Custody",
        "CBP_Transferred",
        "HHS_Care",
        "HHS_Discharged"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col])

    # Sort date
    df = df.sort_values("Date")

    return df