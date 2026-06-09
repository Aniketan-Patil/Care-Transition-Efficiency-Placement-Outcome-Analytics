import streamlit as st

from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis
from utils.feature_engineering import create_features
from utils.risk_detector import detect_risk_levels
from utils.bottleneck_detector import identify_bottlenecks
from utils.filtering import apply_filters

from utils.charts import (
    create_bottleneck_chart,
    create_risk_chart,
    create_discharge_drop_chart
)

st.title("Bottleneck Detection")

full_df = load_and_clean_data()
full_df = calculate_kpis(full_df)
full_df = create_features(full_df)
full_df = detect_risk_levels(full_df)
full_df = identify_bottlenecks(full_df)

df = apply_filters(full_df)

if df.empty:
    st.warning("No records available.")
    st.stop()

st.subheader("Backlog Accumulation Analysis")

backlog_fig = create_bottleneck_chart(df)

st.plotly_chart(
    backlog_fig,
    use_container_width=True
)

current_gap = df["Flow_Gap"].mean()

if current_gap > 20:

    st.error(
        f"Critical backlog accumulation detected ({current_gap:.2f})."
    )

elif current_gap > 5:

    st.warning(
        f"Moderate backlog accumulation detected ({current_gap:.2f})."
    )

else:

    st.success(
        "Pipeline throughput is keeping pace with inflows."
    )

st.divider()

risk_fig = create_risk_chart(df)

st.plotly_chart(
    risk_fig,
    use_container_width=True
)

st.divider()

st.subheader(
    "Sudden Reunification Changes"
)

st.plotly_chart(
    create_discharge_drop_chart(df),
    use_container_width=True
)

drop_days = df[
    df["Sudden_Drop"] < -20
]

if len(drop_days) > 0:

    st.error(
        f"{len(drop_days)} significant discharge drops detected."
    )

else:

    st.success(
        "No major discharge performance drops detected."
    )

st.divider()

st.subheader(
    "Stagnation Monitoring"
)

stagnation_days = df[
    df["Backlog_Rate"]
    >
    df["Backlog_Rate"].mean()
]

st.info(
    f"Potential prolonged stagnation periods detected: {len(stagnation_days)}"
)