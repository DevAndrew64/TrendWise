from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

def train_model(data, column):
    data['timestamp'] = data.index.astype('int64') // 10**9
    X = data['timestamp'].values.reshape(-1, 1)
    y = data[column].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)
    
    return model
