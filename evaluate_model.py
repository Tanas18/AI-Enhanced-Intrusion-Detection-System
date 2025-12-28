import joblib
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix

# Load data
X_train, X_test, y_train, y_test = joblib.load("data/processed_data.pkl")

# Load model
model = tf.keras.models.load_model("model.h5")

# Predict
y_pred = model.predict(X_test).argmax(axis=1)

# Evaluation report
print("📊 Classification Report:")
print(classification_report(y_test, y_pred))

print("🧩 Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
