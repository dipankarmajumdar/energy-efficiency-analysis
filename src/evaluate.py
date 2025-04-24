from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    results = {
        "Heating Load": {
            "MAE": mean_absolute_error(y_test.iloc[:, 0], y_pred[:, 0]),
            "RMSE": np.sqrt(mean_squared_error(y_test.iloc[:, 0], y_pred[:, 0])),
            "R2": r2_score(y_test.iloc[:, 0], y_pred[:, 0])
        },
        "Cooling Load": {
            "MAE": mean_absolute_error(y_test.iloc[:, 1], y_pred[:, 1]),
            "RMSE": np.sqrt(mean_squared_error(y_test.iloc[:, 1], y_pred[:, 1])),
            "R2": r2_score(y_test.iloc[:, 1], y_pred[:, 1])
        }
    }
    return results