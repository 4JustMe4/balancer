from catboost import CatBoostClassifier, CatBoostRegressor
from utils import readClassifire, readRegressor, printClfMetrics, printRegMetrics, splitClfDataset, splitRegDataset


def trainCatboostClf():
    X_clf, y_clf, cat_features_clf = readClassifire()
    Xc_train, Xc_test, yc_train, yc_test = splitClfDataset(X_clf, y_clf)

    clf = CatBoostClassifier(iterations=300, verbose=100)
    clf.fit(Xc_train, yc_train, cat_features=cat_features_clf, eval_set=(Xc_test, yc_test))

    y_pred_clf = clf.predict(Xc_test)
    y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

    printClfMetrics("CatBoost", yc_test, y_pred_clf, y_prob_clf)
    clf.save_model("../data/catboost_success_model.cbm")


def trainCatboostReg():
    X_reg, y_reg, cat_features_reg = readRegressor()
    Xr_train, Xr_test, yr_train, yr_test = splitRegDataset(X_reg, y_reg)

    reg = CatBoostRegressor(iterations=300, verbose=100)
    reg.fit(Xr_train, yr_train, cat_features=cat_features_reg, eval_set=(Xr_test, yr_test))

    y_pred_reg = reg.predict(Xr_test)

    printRegMetrics("CatBoost", yr_test, y_pred_reg)
    reg.save_model("../data/catboost_time_model.cbm")

if __name__ == "__main__":
    trainCatboostClf()
    trainCatboostReg()
