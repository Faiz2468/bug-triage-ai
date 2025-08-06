import streamlit as st
import pandas as pd
import joblib
from sentence_transformers import SentenceTransformer
from utils import preprocess

# Load models
st.session_state.setdefault('model', joblib.load("models/classifier_multi.pkl"))
st.session_state.setdefault('embedder', joblib.load("models/bert_embedder.pkl"))
st.session_state.setdefault('encoders', joblib.load("models/label_encoders.pkl"))

st.title("🛠️ Bug Triage AI")
st.markdown("Enter a bug report and get predictions for **label**, **severity**, **priority**, and **team**.")

# User Input
title = st.text_input("Title", "Crash on login with valid credentials")
description = st.text_area("Description", "App crashes when user logs in using valid credentials.")

if st.button("Predict"):
    # Preprocess input
    df_input = pd.DataFrame([{
        "title": title,
        "description": description
    }])
    df_input = preprocess(df_input)
    text_input = df_input["text"].tolist()

    # BERT embedding
    embedder = st.session_state.embedder
    text_emb = embedder.encode(text_input)

    # Prediction
    model = st.session_state.model
    y_pred = model.predict(text_emb)

    encoders = st.session_state.encoders
    target_cols = ['label', 'severity', 'priority', 'team']

    results = {
        col: encoders[col].inverse_transform([y_pred[0][i]])[0]
        for i, col in enumerate(target_cols)
    }

    # Display
    st.subheader("🔮 Prediction Results")
    for key, value in results.items():
        st.write(f"**{key.capitalize()}**: {value}")