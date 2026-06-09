def identify_bottlenecks(df):

    df["Flow_Gap"] = (
        df["CBP_Apprehended"]
        - df["HHS_Discharged"]
    )

    df["Bottleneck_Flag"] = (
        df["Flow_Gap"] > 0
    )

    return df