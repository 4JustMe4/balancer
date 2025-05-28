import pandas as pd
import joblib

from xgboost import XGBClassifier, XGBRegressor
from utils import readClassifire, readRegressor, printClfMetrics, printRegMetrics, splitClfDataset, splitRegDataset, sanitizeNames

def trainXGBoostClf():
    X_clf, y_clf, cat_features_clf = readClassifire()
    X_clf = sanitizeNames(pd.get_dummies(X_clf, columns=cat_features_clf))
    Xc_train, Xc_test, yc_train, yc_test = splitClfDataset(X_clf, y_clf)

    clf = XGBClassifier(n_estimators=300, use_label_encoder=False, eval_metric='logloss', verbosity=1)
    clf.fit(Xc_train, yc_train, eval_set=[(Xc_test, yc_test)], verbose=100)

    y_pred_clf = clf.predict(Xc_test)
    y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

    printClfMetrics("XGBoost", yc_test, y_pred_clf, y_prob_clf)
    joblib.dump(clf, "../data/xgboost_success_model.joblib")


def trainXGBoostReg():
    X_reg, y_reg, cat_features_reg = readRegressor()
    X_reg = sanitizeNames(pd.get_dummies(X_reg, columns=cat_features_reg))
    Xr_train, Xr_test, yr_train, yr_test = splitRegDataset(X_reg, y_reg)

    reg = XGBRegressor(n_estimators=300, verbosity=1)
    reg.fit(Xr_train, yr_train, eval_set=[(Xr_test, yr_test)], verbose=100)

    y_pred_reg = reg.predict(Xr_test)

    printRegMetrics("XGBoost", yr_test, y_pred_reg)

    joblib.dump(reg, "../data/xgboost_time_model.joblib")


if __name__ == "__main__":
    trainXGBoostClf()
    trainXGBoostReg()
