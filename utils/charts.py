import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


def create_transfer_chart(df):

    fig = px.line(
        df,
        x="Date",
        y="Transfer_Efficiency",
        title="Transfer Efficiency Over Time"
    )

    return fig

def create_risk_chart(df):

    risk_counts = (
        df["Risk_Level"]
        .value_counts()
        .reset_index()
    )

    risk_counts.columns = [
        "Risk_Level",
        "Count"
    ]

    fig = px.pie(
        risk_counts,
        names="Risk_Level",
        values="Count",
        title="Risk Distribution"
    )

    return fig

def create_bottleneck_chart(df):

    fig = px.line(
        df,
        x="Date",
        y="Flow_Gap",
        title="Backlog Accumulation Trend"
    )

    return fig


def create_monthly_discharge_chart(df):

    import plotly.express as px

    monthly = (
        df.groupby(["Year", "Month"])
        ["HHS_Discharged"]
        .sum()
        .reset_index()
    )

    monthly["Period"] = (
        monthly["Year"].astype(str)
        + "-"
        + monthly["Month"].astype(str)
    )

    fig = px.bar(
        monthly,
        x="Period",
        y="HHS_Discharged",
        title="Monthly Sponsor Placements"
    )

    return fig

def create_weekday_analysis_chart(df):

    import plotly.express as px

    weekday = (
        df.groupby("Weekday")
        ["Transfer_Efficiency"]
        .mean()
        .reset_index()
    )

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]

    weekday["Weekday"] = pd.Categorical(
        weekday["Weekday"],
        categories=weekday_order,
        ordered=True
    )

    weekday = weekday.sort_values("Weekday")

    fig = px.bar(
        weekday,
        x="Weekday",
        y="Transfer_Efficiency",
        title="Weekday vs Weekend Transfer Efficiency"
    )

    return fig


def create_forecast_chart(
    actual,
    predicted
):

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            y=actual,
            mode="lines",
            name="Actual"
        )
    )

    fig.add_trace(
        go.Scatter(
            y=predicted,
            mode="lines",
            name="Predicted"
        )
    )

    fig.update_layout(
        title="HHS Discharge Forecast Performance"
    )

    return fig

def create_outcome_stability_chart(df):

    fig = px.line(
        df,
        x="Date",
        y="Outcome_Stability_Score",
        title="Outcome Stability Over Time"
    )

    return fig

def create_discharge_drop_chart(df):

    fig = px.bar(
        df,
        x="Date",
        y="Sudden_Drop",
        title="Sudden Changes in Reunification Outcomes"
    )

    return fig