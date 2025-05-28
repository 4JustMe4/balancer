from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score
)
import numpy as np

from utils import *

X_clf, y_clf, cat_features_clf = readClassifire()
Xc_train, Xc_test, yc_train, yc_test = splitDataset(X_clf, y_clf)

clf = CatBoostClassifier(iterations=300, verbose=100)
clf.fit(Xc_train, yc_train, cat_features=cat_features_clf, eval_set=(Xc_test, yc_test))

y_pred_clf = clf.predict(Xc_test)
y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

printClfMetrics(yc_test, y_pred_clf, y_prob_clf)

X_reg, y_reg, cat_features_reg = readRegressor()
Xr_train, Xr_test, yr_train, yr_test = splitDataset(X_reg, y_reg)

reg = CatBoostRegressor(iterations=300, verbose=100)
reg.fit(Xr_train, yr_train, cat_features=cat_features_reg, eval_set=(Xr_test, yr_test))

y_pred_reg = reg.predict(Xr_test)

mae = mean_absolute_error(yr_test, y_pred_reg)
rmse = np.sqrt(mean_squared_error(yr_test, y_pred_reg))
r2 = r2_score(yr_test, y_pred_reg)

print(f"MAE:  {mae:.4f}   # (средняя абсолютная ошибка)")
print(f"RMSE: {rmse:.4f}   # (корень среднеквадратичной ошибки)")
print(f"R²:   {r2:.4f}   # (коэффициент детерминации)")


clf.save_model("../data/catboost_success_model.cbm")
reg.save_model("../data/catboost_time_model.cbm")