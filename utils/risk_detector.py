import numpy as np


def detect_risk_levels(df):

    conditions = [

        (
            (df["Transfer_Efficiency"] < 20)
            |
            (df["Discharge_Effectiveness"] < 0.2)
        ),

        (
            (df["Transfer_Efficiency"] < 40)
            |
            (df["Discharge_Effectiveness"] < 0.5)
        )

    ]

    choices = [
        "Critical",
        "Warning"
    ]

    df["Risk_Level"] = np.select(
        conditions,
        choices,
        default="Normal"
    )

    return df