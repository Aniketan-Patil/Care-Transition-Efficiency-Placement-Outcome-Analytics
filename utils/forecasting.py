from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from sklearn.ensemble import RandomForestRegressor


def forecast_discharge(df):

    data = df.copy()

    data["Lag_1"] = data["HHS_Discharged"].shift(1)
    data["Lag_7"] = data["HHS_Discharged"].shift(7)
    data["Lag_14"] = data["HHS_Discharged"].shift(14)

    data["Lag_30"] = data["HHS_Discharged"].shift(30)

    data["RollingMean_7"] = (
    data["HHS_Discharged"]
    .rolling(7)
    .mean()
    )

    data["RollingMean_30"] = (
    data["HHS_Discharged"]
    .rolling(30)
    .mean()
    )

    data["RollingStd_7"] = (
    data["HHS_Discharged"]
    .rolling(7)
    .std()
    )

    data["Lag_1"] = data["HHS_Discharged"].shift(1)
    data["Lag_7"] = data["HHS_Discharged"].shift(7)
    data["Lag_14"] = data["HHS_Discharged"].shift(14)

    data["Lag_30"] = data["HHS_Discharged"].shift(30)

    data["RollingMean_7"] = (
    data["HHS_Discharged"]
    .rolling(7)
    .mean()
    )

    data["RollingMean_30"] = (
    data["HHS_Discharged"]
    .rolling(30)
    .mean()
    )

    data["RollingStd_7"] = (
    data["HHS_Discharged"]
    .rolling(7)
    .std()
    )

    data = data.dropna()

    features = [
    "Year",
    "Month",
    "Quarter",
    "DayOfWeek",

    "Lag_1",
    "Lag_7",
    "Lag_14",
    "Lag_30",

    "RollingMean_7",
    "RollingMean_30",
    "RollingStd_7"
    ]

    X = data[features]

    y = data["HHS_Discharged"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        shuffle=False
    )

    model = RandomForestRegressor(
    n_estimators=500,
    max_depth=12,
    min_samples_split=5,
    random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mae = mean_absolute_error(y_test, predictions)

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(
        y_test,
        predictions
    )

    return predictions, y_test, mae, rmse, r2