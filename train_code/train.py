import pandas as pd
import pickle
import lightgbm as lgb
from sklearn.model_selection import train_test_split

class LightGBMWrapper(object):
    def __init__(self, seed=0, params=None):
        params['feature_fraction_seed'] = seed
        params['bagging_seed'] = seed
        self.params = params
        
    def train(self, X_train, y_train, X_val, y_val, num_boost_round=100000, early_stopping_rounds=100, verbose_eval=100):
        
        lgb_train = lgb.Dataset(X_train,y_train)  
        lgb_valid = lgb.Dataset(X_val,y_val)
        self.clf = lgb.train(params=self.params, 
                         train_set=lgb_train,
                         valid_sets=[lgb_train, lgb_valid],
                         num_boost_round=num_boost_round,   
                         verbose_eval=verbose_eval,
                         early_stopping_rounds=early_stopping_rounds,
                        )
        
    def predict(self, x):
        return self.clf.predict(x)

train = pd.read_csv('data/train.csv')

X_train = train.drop('target', axis=1)
y_train = train['target']

X_train, X_val, y_train, y_val = train_test_split(X_train, y_train)

params = {
    'boosting_type' : 'gbdt',
    'objective' : 'regression',
    'colsample_bytree' : 0.5,
    'max_depth' : 10,
    'learning_rate' : 0.05,
    'seed' : 0,
    'metric' : 'rmse',
    'min_data_in_leaf' : 2
}

model = LightGBMWrapper(params=params)

model.train(X_train, y_train, X_val, y_val,early_stopping_rounds=10, verbose_eval=100)


filename = 'model/lgb.pkl'
pickle.dump(model, open(filename, 'wb'))









