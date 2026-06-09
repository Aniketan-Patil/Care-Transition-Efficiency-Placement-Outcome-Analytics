from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis
from utils.feature_engineering import create_features
from utils.risk_detector import detect_risk_levels

df = load_and_clean_data()

df = calculate_kpis(df)

df = create_features(df)

df = detect_risk_levels(df)

print(df.head())

print("\nColumns:\n")

print(df.columns)

print("\nRisk Counts:\n")

print(df["Risk_Level"].value_counts())