import streamlit as st

from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis
from utils.feature_engineering import create_features
from utils.risk_detector import detect_risk_levels
from utils.bottleneck_detector import identify_bottlenecks
from utils.filtering import apply_filters
from utils.executive_metrics import calculate_summary_metrics
from utils.charts import create_risk_chart
from utils.forecasting import forecast_discharge
from utils.pdf_generator import generate_pdf_report
from utils.charts import create_outcome_stability_chart

st.title("Executive Dashboard")
show_ratios = st.sidebar.checkbox(
    "Show Ratio Metrics",
    value=True
)

full_df = load_and_clean_data()
full_df = calculate_kpis(full_df)
full_df = create_features(full_df)
full_df = detect_risk_levels(full_df)
full_df = identify_bottlenecks(full_df)

df = apply_filters(full_df)

if df.empty:
    st.warning("No records available.")
    st.stop()

metrics = calculate_summary_metrics(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Apprehended",
        f"{metrics['Total Apprehended']:,}"
    )

with col2:
    st.metric(
        "Total Transfers",
        f"{metrics['Total Transfers']:,}"
    )

with col3:
    st.metric(
        "Total Discharged",
        f"{metrics['Total Discharged']:,}"
    )

with col4:
    st.metric(
        "Pipeline Throughput",
        f"{df['Pipeline_Throughput'].mean():.2f}%"
    )
st.divider()



risk_fig = create_risk_chart(df)

st.plotly_chart(
    risk_fig,
    use_container_width=True
)

st.divider()

predictions, actual, mae, rmse, r2 = (
    forecast_discharge(full_df)
)

st.subheader("Executive Report")

full_metrics = calculate_summary_metrics(full_df)

pdf_file = generate_pdf_report(
    full_metrics,
    mae,
    rmse,
    r2,
    full_df
)

with open(pdf_file, "rb") as file:

    st.download_button(
        label="📄 Download Executive Report",
        data=file,
        file_name="Care_Transition_Report.pdf",
        mime="application/pdf"
    )

st.divider()

col5, col6 = st.columns(2)

with col5:
    st.metric(
        "Outcome Stability",
        f"{df['Outcome_Stability_Score'].mean():.2f}"
    )

with col6:
    st.metric(
        "Average Backlog Rate",
        f"{df['Backlog_Rate'].mean():.2f}"
    )

st.divider()

st.subheader(
    "Outcome Stability Analysis"
)

st.plotly_chart(
    create_outcome_stability_chart(df),
    use_container_width=True
)

if show_ratios:

    st.divider()

    st.subheader(
        "Ratio Metrics"
    )

    r1, r2 = st.columns(2)

    with r1:

        st.metric(
            "Transfer Efficiency",
            f"{df['Transfer_Efficiency'].mean():.2f}%"
        )

    with r2:

        st.metric(
            "Discharge Effectiveness",
            f"{df['Discharge_Effectiveness'].mean():.2f}%"
        )