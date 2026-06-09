from utils.data_preprocessing import load_and_clean_data

df = load_and_clean_data()

print("Min Date:", df["Date"].min())
print("Max Date:", df["Date"].max())

print("\nTotal Records:", len(df))

# Check for duplicate dates
duplicates = df["Date"].duplicated().sum()

print("\nDuplicate Dates:", duplicates)

# Check for invalid dates
print("\nNull Dates:", df["Date"].isnull().sum())