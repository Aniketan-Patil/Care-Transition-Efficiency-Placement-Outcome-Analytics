import streamlit as st

from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis
from utils.feature_engineering import create_features
from utils.risk_detector import detect_risk_levels
from utils.bottleneck_detector import identify_bottlenecks
from utils.filtering import apply_filters
from utils.sankey_charts import create_pipeline_sankey

from utils.charts import (
    create_transfer_chart,
    create_monthly_discharge_chart,
    create_weekday_analysis_chart
)

st.title("Pipeline Analysis")

full_df = load_and_clean_data()
full_df = calculate_kpis(full_df)
full_df = create_features(full_df)
full_df = detect_risk_levels(full_df)
full_df = identify_bottlenecks(full_df)

df = apply_filters(full_df)

if df.empty:
    st.warning("No records available.")
    st.stop()

st.subheader("Care Pipeline Flow")

sankey_fig = create_pipeline_sankey(df)

st.plotly_chart(
    sankey_fig,
    use_container_width=True
)

st.divider()

st.subheader("Transfer Efficiency")

transfer_fig = create_transfer_chart(df)

st.plotly_chart(
    transfer_fig,
    use_container_width=True
)

st.divider()

st.subheader("Monthly Placement Trends")

monthly_fig = create_monthly_discharge_chart(df)

st.plotly_chart(
    monthly_fig,
    use_container_width=True
)

st.divider()

st.subheader("Weekday vs Weekend Analysis")

weekday_fig = create_weekday_analysis_chart(df)

st.plotly_chart(
    weekday_fig,
    use_container_width=True
)