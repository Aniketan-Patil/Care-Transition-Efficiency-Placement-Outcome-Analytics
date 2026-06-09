import streamlit as st


def apply_filters(df):

    min_date = df["Date"].min()

    max_date = df["Date"].max()

    st.sidebar.header("Filters")

    selected_dates = st.sidebar.date_input(
        "Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if len(selected_dates) == 2:

        start_date, end_date = selected_dates

        df = df[
            (df["Date"] >= str(start_date))
            &
            (df["Date"] <= str(end_date))
        ]

    return df