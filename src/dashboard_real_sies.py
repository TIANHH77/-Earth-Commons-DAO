import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SUR DAO Dashboard", layout="wide")
st.title("🌑 SUR DAO - Capa Sombra Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/surdao_real_matches_2025.csv")

df = load_data()

# --- Definir pestañas ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["📊 KPIs", "📄 Tabla", "📊 Barras", "📈 Scatter", "🔵 Bubble Chart"]
)





