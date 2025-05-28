from train_catboost import trainCatboostClf, trainCatboostReg
from train_random_forest import trainRandomForestClf, trainRandomForestReg
from train_logres import trainLogResClf, trainLogResReg
from train_xgboost import trainXGBoostClf, trainXGBoostReg

if __name__ == "__main__":
    print('Classifier')
    trainLogResClf()
    trainCatboostClf()
    trainRandomForestClf()
    trainXGBoostClf()

    print('\n' * 3 + 'Regressor')
    trainLogResReg()
    trainCatboostReg()
    trainRandomForestReg()
    trainXGBoostReg()
