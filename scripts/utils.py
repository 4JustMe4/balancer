import pandas as pd
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, roc_auc_score, precision_score, recall_score, f1_score,
    mean_absolute_error, mean_squared_error, r2_score
)

EXCLUDE_CLF = [
    'result_id','host_id','workunit_id','result_create_time',
    'cpu_time','elapsed_time','exit_status','flops_estimate',
    'peak_working_set_size','peak_disk_usage','peak_swap_size',
    'success','outcome', 'client_state', 'workunit_create_time', 'wu_error_mask', 
]

EXCLUDE_REG = EXCLUDE_CLF + [
    'server_state','outcome','client_state','host_id',
    'p_ncpus','p_vendor','p_model','p_fpops','p_iops','p_membw',
    'os_name','os_version','m_nbytes','m_cache','m_swap','d_total',
    'd_free','d_boinc_used_total','d_boinc_used_project','d_boinc_max',
    'n_bwup','n_bwdown','cpu_efficiency','duration_correction_factor','error_rate',
    'gpu_active_frac','p_ngpus','p_gpu_fpops'
]


def splitClfDataset(X, y):
    return train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)


def splitRegDataset(X, y):
    return train_test_split(X, y, test_size=0.2, random_state=42)


def readDataSet():
    beg = 2066
    SIZE = 20
    df1 = pd.read_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part1.csv')
    df2 = pd.read_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part2.csv')
    df3 = pd.read_csv(f'../data/df_with_matrix_{SIZE}_{beg}_part3.csv')
    df = pd.concat([df1, df2, df3], ignore_index=True)
    df['success'] = (df['outcome'] == 1).astype(int)
    mask = df['success'] == 1
    zero_idxs = df.index[mask]
    n_replace = int(len(zero_idxs) * 0.01)
    if n_replace > 0:
        np.random.seed(42)
        replace_idxs = np.random.choice(zero_idxs, size=n_replace, replace=False)
        df.loc[replace_idxs, 'success'] = 0
    return df


def readClassifire():
    df = readDataSet()
    
    features_clf = [c for c in df.columns if c not in EXCLUDE_CLF]
    mat_cols = [col for col in df.columns if col.startswith('mat_')]
    cat_features_clf = [c for c in features_clf if df[c].dtype == 'object' or c.startswith('mat_')]
    
    for col in mat_cols:
        df[col] = df[col].fillna(-1).astype(int)
    
    return df[features_clf], df['success'], cat_features_clf


def readRegressor():
    df = readDataSet()
    
    features_reg = [c for c in df.columns if c not in EXCLUDE_REG]
    mat_cols = [col for col in df.columns if col.startswith('mat_')]
    cat_features_reg = [c for c in features_reg if df[c].dtype == 'object']
    
    for col in mat_cols:
        df[col] = df[col].fillna(-1).astype(int)

    return df[features_reg], df['cpu_time'], cat_features_reg


def printClfMetrics(name, yc_test, y_pred_clf, y_prob_clf):
    print(f'Metrix for {name}')
    print(f"Accuracy:  {accuracy_score(yc_test, y_pred_clf):.4f}     # (доля верных ответов)")
    print(f"ROC-AUC:   {roc_auc_score(yc_test, y_prob_clf):.4f}     # (чувствительность vs 1-специфичность)")
    print(f"Precision: {precision_score(yc_test, y_pred_clf):.4f}     # (точность: TP / (TP+FP))")
    print(f"Recall:    {recall_score(yc_test, y_pred_clf):.4f}     # (полнота: TP / (TP+FN))")
    print(f"F1-score:  {f1_score(yc_test, y_pred_clf):.4f}     # (гармоническое среднее precision и recall)")


def printRegMetrics(name, yr_test, y_pred_reg):
    mae = mean_absolute_error(yr_test, y_pred_reg)
    rmse = np.sqrt(mean_squared_error(yr_test, y_pred_reg))
    r2 = r2_score(yr_test, y_pred_reg)
    print(f'Metrix for {name}')
    print(f"MAE:  {mae:.4f}   # (средняя абсолютная ошибка)")
    print(f"RMSE: {rmse:.4f}   # (корень среднеквадратичной ошибки)")
    print(f"R²:   {r2:.4f}   # (коэффициент детерминации)")


def sanitizeNames(df):
    df.columns = (
        df.columns
        .str.replace(r"\[", "_", regex=True)
        .str.replace(r"\]", "_", regex=True)
        .str.replace(r"<", "_", regex=True)
        .str.replace(r">", "_", regex=True)
    )
    return df


def getSparse(X, y, frac=0.1, random_state=42):
    X_sparse, _, y_sparse, _ = train_test_split(
        X, y, train_size=frac, random_state=random_state
    )
    return X_sparse, y_sparse

def dumpAndCompress(model, path):
    joblib.dump(model, path, compress=3)