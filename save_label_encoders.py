import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from utils import preprocess

print("📦 Loading dataset...")
df = pd.read_csv("data/bugs.csv")

print("🧼 Preprocessing...")
df = preprocess(df)

# Restore original target columns
df_raw = pd.read_csv("data/bugs.csv")
for col in ['label', 'severity', 'priority', 'team']:
    if col in df_raw.columns:
        df[col] = df_raw[col]

print("🧾 Columns in dataframe:")
print(df.columns.tolist())

# 🔧 Encode labels
label_encoders = {}
target_cols = ['label', 'severity', 'priority', 'team']

print("🔧 Encoding labels...")
for col in target_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le
    print(f"✅ Encoded: {col}")

# 💾 Save to disk
os.makedirs("models", exist_ok=True)
joblib.dump(label_encoders, "models/label_encoders.pkl")
print("✅ Label encoders saved to 'models/label_encoders.pkl'")