from utils.data_preprocessing import load_and_clean_data
from utils.kpi_calculator import calculate_kpis

df = load_and_clean_data()

df = calculate_kpis(df)

print(df.head())

print("\n")

print(df.columns)