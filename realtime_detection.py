import tensorflow as tf
import numpy as np
import time

# Load trained model
model = tf.keras.models.load_model("model.h5")

print("🛡️ Real-Time Intrusion Detection Started (Simulation)")
print("Press Ctrl + C to stop\n")

try:
    while True:
        # Simulated network packet features
        packet_features = np.random.rand(1, model.input_shape[1])

        prediction = model.predict(packet_features, verbose=0)
        label = prediction.argmax()

        if label == 0:
            print("✅ Normal Traffic")
        else:
            print("🚨 ATTACK DETECTED")

        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Detection stopped")
