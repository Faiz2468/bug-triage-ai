from sentence_transformers import SentenceTransformer
import joblib
import os

print("📁 Ensuring models directory exists...")
os.makedirs("models", exist_ok=True)

print("🔄 Loading SentenceTransformer model...")
embedder = SentenceTransformer("all-MiniLM-L6-v2")
print("✅ Embedder loaded.")

print("💾 Saving embedder to 'models/bert_embedder.pkl' ...")
joblib.dump(embedder, "models/bert_embedder.pkl")
print("✅ Embedder saved successfully.")