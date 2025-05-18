import pandas as pd

df = pd.read_csv("../data/df_with_matrix.csv")

from sklearn.model_selection import train_test_split

# Оставляем только строки с ненулевым cpu_time (если есть ошибки/NaN, их лучше убрать)
df = df[df['cpu_time'].notnull()]

# Признаки — всё кроме целевой переменной и, возможно, идентификаторов
features = [col for col in df.columns if col not in ['cpu_time', 'result_id', 'workunit_id', 'host_id']]

X = df[features]
y = df['cpu_time']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from catboost import CatBoostRegressor

# Если есть категориальные признаки — добавьте их в cat_features (например, os_name, p_vendor, p_model)
cat_features = [col for col in ['os_name', 'p_vendor', 'p_model', 'os_version'] if col in X_train.columns]

model = CatBoostRegressor(
    iterations=500,
    learning_rate=0.1,
    depth=8,
    loss_function='RMSE',
    verbose=100
)

model.fit(X_train, y_train, cat_features=cat_features, eval_set=(X_test, y_test))

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, y_pred))
print("RMSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))