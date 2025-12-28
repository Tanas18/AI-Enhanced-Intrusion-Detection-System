import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
df = pd.read_csv("data/CICIDS2017.csv")

# 🔹 FIX: remove leading/trailing spaces in column names
df.columns = df.columns.str.strip()

# Remove duplicates
df = df.drop_duplicates()

# Handle infinite and missing values
df = df.replace([float('inf'), -float('inf')], 0)
df = df.fillna(0)

# Encode labels
label_encoder = LabelEncoder()
df['Label'] = label_encoder.fit_transform(df['Label'])

# Split features and target
X = df.drop('Label', axis=1)
y = df['Label']

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Save processed data
joblib.dump((X_train, X_test, y_train, y_test), "data/processed_data.pkl")

print("✅ Preprocessing finished successfully")
