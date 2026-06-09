from utils.data_preprocessing import load_and_clean_data

df = load_and_clean_data()

print("Rows:", len(df))

print("Null Values:\n")
print(df.isnull().sum())