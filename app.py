import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

st.set_page_config(page_title="Hierarchical Clustering", layout="centered")

st.title("🎓 Hierarchical Clustering – Universities Dataset")

# Load dataset
df = pd.read_csv("Universities.csv")

# Feature selection (excluding university name column)
X = df.iloc[:, 1:]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Model training (NO pickle)
model = AgglomerativeClustering(n_clusters=3)
clusters = model.fit_predict(X_scaled)

df["Cluster"] = clusters

st.subheader("📊 Clustered Universities")
st.dataframe(df)

st.success("Model trained dynamically. No pickle file used.")
