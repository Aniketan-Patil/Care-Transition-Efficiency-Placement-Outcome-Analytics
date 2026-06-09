import pandas as pd

def calculate_summary_metrics(df):

    if df.empty:

        return {
            "Total Apprehended": 0,
            "Total Transfers": 0,
            "Total Discharged": 0,
            "Average HHS Care": 0,
            "Avg Transfer Efficiency": 0,
            "Avg Discharge Effectiveness": 0
        }

    return {

        "Total Apprehended":
        int(df["CBP_Apprehended"].sum()),

        "Total Transfers":
        int(df["CBP_Transferred"].sum()),

        "Total Discharged":
        int(df["HHS_Discharged"].sum()),

        "Average HHS Care":
        round(df["HHS_Care"].mean(), 0),

        "Avg Transfer Efficiency":
        round(df["Transfer_Efficiency"].mean(), 2),

        "Avg Discharge Effectiveness":
        round(df["Discharge_Effectiveness"].mean(), 2)
    }