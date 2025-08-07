import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib
import os
from utils import preprocess

# load the csv plssssss so tired
df = pd.read_csv("data/bugs.csv")

# clean
df = preprocess(df)

# whose there open the door
print("Columns in dataframe:")
print(df.columns.tolist())

# folder want to save stuff
os.makedirs("models", exist_ok=True)

# labels to encode again ughhh
label_cols = ['product', 'component', 'priority', 'severity']

# rinse and repeat for each column
for col in label_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    joblib.dump(le, f"models/{col}_encoder.pkl")  # save the encoder file
    print(f"Saved encoder for '{col}' to models/{col}_encoder.pkl")