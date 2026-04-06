import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

def train_model():
    data = pd.read_csv("data/sample_data.csv")
    X = data.drop(['footfall','date'], axis=1)
    y = data['footfall']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = XGBRegressor()
    model.fit(X_train, y_train)
    return model
