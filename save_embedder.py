from sentence_transformers import SentenceTransformer
import joblib
import os

# is the folder there?
os.makedirs("models", exist_ok=True)

# loading model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# save model into a file for later
joblib.dump(embedder, "models/bert_embedder.pkl")
print("saved embedder to models/bert_embedder.pkl")