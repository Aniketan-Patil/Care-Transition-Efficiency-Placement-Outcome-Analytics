import streamlit as st

from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis
from utils.feature_engineering import create_features

from utils.forecasting import forecast_discharge

from utils.charts import create_forecast_chart

st.title("Forecasting")

full_df = load_and_clean_data()

full_df = calculate_kpis(full_df)

full_df = create_features(full_df)

predictions, actual, mae, rmse, r2 = (
    forecast_discharge(full_df)
)

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "MAE",
        f"{mae:.2f}"
    )

with c2:
    st.metric(
        "RMSE",
        f"{rmse:.2f}"
    )

with c3:
    st.metric(
        "R² Score",
        f"{r2:.3f}"
    )

forecast_fig = create_forecast_chart(
    actual,
    predictions
)

st.plotly_chart(
    forecast_fig,
    use_container_width=True
)