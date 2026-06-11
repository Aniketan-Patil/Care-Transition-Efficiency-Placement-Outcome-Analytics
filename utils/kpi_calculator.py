import numpy as np


def calculate_kpis(df):

    # Transfer Efficiency Ratio

    df["Transfer_Efficiency"] = np.where(
        df["CBP_Custody"] == 0,
        0,
        (
            df["CBP_Transferred"]
            / df["CBP_Custody"]
        ) * 100
    )

    # Discharge Effectiveness

    df["Discharge_Effectiveness"] = np.where(
        df["HHS_Care"] == 0,
        0,
        (
            df["HHS_Discharged"]
            / df["HHS_Care"]
        ) * 100
    )

    # Pipeline Throughput

    df["Pipeline_Throughput"] = np.where(
    df["CBP_Transferred"] == 0,
    0,
    np.minimum(
        (
            df["HHS_Discharged"]
            / df["CBP_Transferred"]
        ) * 100,
        100
    )
)

    # Backlog Accumulation Rate
    df["Backlog_Rate"] = np.maximum(
        df["CBP_Apprehended"]
        - df["HHS_Discharged"],
        0
)

    # Outcome Stability Score

    rolling_std = (
        df["HHS_Discharged"]
        .rolling(window=30)
        .std()
    )

    df["Outcome_Stability_Score"] = (
        100 / (1 + rolling_std)
    )

    # Clean Infinite and Missing Values

    df.replace(
        [np.inf, -np.inf],
        0,
        inplace=True
    )

    df.fillna(
        0,
        inplace=True
    )

    return df