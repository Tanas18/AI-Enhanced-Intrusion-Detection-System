import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Load processed data
X_train, X_test, y_train, y_test = joblib.load("data/processed_data.pkl")

# Build Neural Network
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(32, activation='relu'))
model.add(Dense(len(set(y_train)), activation='softmax'))

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(X_train, y_train, epochs=10, batch_size=64)

# Save model
model.save("model.h5")

print("✅ Model trained and saved successfully")
