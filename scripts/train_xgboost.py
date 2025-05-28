import pandas as pd
import numpy as np

from xgboost import XGBClassifier, XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score
)
import joblib

df = pd.read_csv('../data/df_with_matrix.csv')

df['success'] = (df['outcome'] == 1).astype(int)

def clean_column_names(df):
    df.columns = (
        df.columns
        .str.replace(r"\[", "_", regex=True)
        .str.replace(r"\]", "_", regex=True)
        .str.replace(r"<", "_", regex=True)
        .str.replace(r">", "_", regex=True)
    )
    return df

exclude_clf = [
    'result_id','host_id','workunit_id','result_create_time',
    'cpu_time','elapsed_time','exit_status','flops_estimate',
    'peak_working_set_size','peak_disk_usage','peak_swap_size',
    'success','outcome', 'client_state', 'workunit_create_time', 'wu_error_mask', 
]
features_clf = [c for c in df.columns if c not in exclude_clf]
mat_cols = [col for col in df.columns if col.startswith('mat_')]

for col in mat_cols:
    df[col] = df[col].fillna(-1).astype(int)

cat_features_clf = [c for c in features_clf if df[c].dtype == 'object' or c.startswith('mat_')]

# XGBoost не умеет работать с категориальными напрямую в sklearn API, нужно закодировать:
X_clf = clean_column_names(pd.get_dummies(df[features_clf], columns=cat_features_clf))
y_clf = df['success']
Xc_train, Xc_test, yc_train, yc_test = train_test_split(
    X_clf, y_clf, stratify=y_clf, test_size=0.2, random_state=42
)

clf = XGBClassifier(n_estimators=300, use_label_encoder=False, eval_metric='logloss', verbosity=1)
clf.fit(Xc_train, yc_train, eval_set=[(Xc_test, yc_test)], verbose=100)

y_pred_clf = clf.predict(Xc_test)
y_prob_clf = clf.predict_proba(Xc_test)[:, 1]

print(f"Accuracy:  {accuracy_score(yc_test, y_pred_clf):.4f}  # (доля верных ответов)")
print(f"ROC-AUC:   {roc_auc_score(yc_test, y_prob_clf):.4f}   # (чувствительность vs 1-специфичность)")
print(f"Precision: {precision_score(yc_test, y_pred_clf):.4f}  # (точность: TP / (TP+FP))")
print(f"Recall:    {recall_score(yc_test, y_pred_clf):.4f}     # (полнота: TP / (TP+FN))")
print(f"F1-score:  {f1_score(yc_test, y_pred_clf):.4f}         # (гармоническое среднее precision и recall)")

exclude_reg = exclude_clf + [
    'server_state','outcome','client_state','host_id',
    'p_ncpus','p_vendor','p_model','p_fpops','p_iops','p_membw',
    'os_name','os_version','m_nbytes','m_cache','m_swap','d_total',
    'd_free','d_boinc_used_total','d_boinc_used_project','d_boinc_max',
    'n_bwup','n_bwdown','cpu_efficiency','duration_correction_factor','error_rate',
    'gpu_active_frac','p_ngpus','p_gpu_fpops'
]
features_reg = [c for c in df.columns if c not in exclude_reg]
cat_features_reg = [c for c in features_reg if df[c].dtype == 'object']

X_reg = clean_column_names(pd.get_dummies(df[features_reg], columns=cat_features_reg))
y_reg = df['cpu_time']
Xr_train, Xr_test, yr_train, yr_test = train_test_split(
    X_reg, y_reg, test_size=0.2, random_state=42
)

reg = XGBRegressor(n_estimators=300, verbosity=1)
reg.fit(Xr_train, yr_train, eval_set=[(Xr_test, yr_test)], verbose=100)

y_pred_reg = reg.predict(Xr_test)

mae = mean_absolute_error(yr_test, y_pred_reg)
rmse = np.sqrt(mean_squared_error(yr_test, y_pred_reg))
r2 = r2_score(yr_test, y_pred_reg)

print(f"MAE:  {mae:.4f}   # (средняя абсолютная ошибка)")
print(f"RMSE: {rmse:.4f}   # (корень среднеквадратичной ошибки)")
print(f"R²:   {r2:.4f}   # (коэффициент детерминации)")

# Сохраняем модели
joblib.dump(clf, "../data/xgboost_success_model.joblib")
joblib.dump(reg, "../data/xgboost_time_model.joblib")
