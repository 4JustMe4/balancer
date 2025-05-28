import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression, LinearRegression
from utils import readClassifire, readRegressor, printClfMetrics, printRegMetrics, splitClfDataset, splitRegDataset, sanitizeNames

def trainLogResClf():
    X_clf, y_clf, cat_features_clf = readClassifire()
    X_clf = sanitizeNames(pd.get_dummies(X_clf, columns=cat_features_clf))
    Xc_train, Xc_test, yc_train, yc_test = splitClfDataset(X_clf, y_clf)

    clf = LogisticRegression(max_iter=1000, solver='lbfgs')
    clf.fit(Xc_train, yc_train)

    y_pred_clf = clf.predict(Xc_test)
    y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

    printClfMetrics("LogRes", yc_test, y_pred_clf, y_prob_clf)
    joblib.dump(clf, "../data/logreg_success_model.joblib")


def trainLogResReg():
    X_reg, y_reg, cat_features_reg = readRegressor()
    X_reg = sanitizeNames(pd.get_dummies(X_reg, columns=cat_features_reg))
    Xr_train, Xr_test, yr_train, yr_test = splitRegDataset(X_reg, y_reg)

    reg = LinearRegression()
    reg.fit(Xr_train, yr_train)

    y_pred_reg = reg.predict(Xr_test)

    printRegMetrics("LogRes", yr_test, y_pred_reg)
    joblib.dump(reg, "../data/linreg_time_model.joblib")


if __name__ == "__main__":
    trainLogResClf()
    trainLogResReg()
