from src.data_preprocessing import load_data, preprocess_data
from src.train_model import train_model, save_model
from src.evaluate import evaluate_model
from src.utils import save_metrics, log

df = load_data("data/uci-energy-efficiency-dataset.csv")
(X_train, X_test, y_train, y_test), scaler = preprocess_data(df)
model = train_model(X_train, y_train)
results = evaluate_model(model, X_test,y_test)
save_model(model)

# After evaluation:
log("Model evaluation completed.")
save_metrics(results)