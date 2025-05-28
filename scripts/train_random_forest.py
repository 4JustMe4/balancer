import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from utils import readClassifire, readRegressor, printClfMetrics, printRegMetrics, splitClfDataset, splitRegDataset, sanitizeNames


def trainRandomForestClf():
    X_clf, y_clf, cat_features_clf = readClassifire()
    X_clf = sanitizeNames(pd.get_dummies(X_clf, columns=cat_features_clf))
    Xc_train, Xc_test, yc_train, yc_test = splitClfDataset(X_clf, y_clf)

    clf = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1)
    clf.fit(Xc_train, yc_train)

    y_pred_clf = clf.predict(Xc_test)
    y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

    printClfMetrics("RandomForest", yc_test, y_pred_clf, y_prob_clf)
    joblib.dump(clf, "../data/rf_success_model.joblib")


def trainRandomForestReg():
    X_reg, y_reg, cat_features_reg = readRegressor()
    X_reg = sanitizeNames(pd.get_dummies(X_reg, columns=cat_features_reg))
    Xr_train, Xr_test, yr_train, yr_test = splitRegDataset(X_reg, y_reg)

    reg = RandomForestRegressor(n_estimators=300, random_state=42, n_jobs=-1)
    reg.fit(Xr_train, yr_train)

    y_pred_reg = reg.predict(Xr_test)

    printRegMetrics("RandomForest", yr_test, y_pred_reg)
    joblib.dump(reg, "../data/rf_time_model.joblib")


if __name__ == "__main__":
    trainRandomForestClf()
    trainRandomForestReg()
