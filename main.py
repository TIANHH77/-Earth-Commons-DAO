import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SUR DAO Dashboard", layout="wide")
st.title("🌑 SUR DAO - Capa Sombra Dashboard")
st.markdown("**Datos reales SIES 2025 + USACH**")

@st.cache_data
def load_data():
    df = pd.read_csv("data/surdao_real_matches_2025.csv")
    return df

df = load_data()

tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 KPIs", "📄 Tabla", "📊 Barras", "📈 Scatter", "🔵 Bubble"])

with tab1:
    st.subheader("📊 KPIs Principales")
    col1, col2, col3 = st.columns(3)
    col1.metric("Carreras", len(df))
    col2.metric("Créditos Acum.", int(df["Creditos_Acum"].sum()))
    col3.metric("Capital $MM", round(df["Capital_Recuperable"].sum(), 2))

with tab2:
    st.subheader("📄 Tabla Completa")
    st.dataframe(df, use_container_width=True)

with tab3:
    st.subheader("📊 Barras Capital")
    fig = px.bar(df.head(10), x="Carrera_SURDAO", y="Capital_Recuperable", 
                 color="Universidad", title="Capital por Carrera")
    st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.subheader("📈 Scatter Deserción vs Capital")
    fig = px.scatter(df.head(20), x="Desercion_SIES_pct", y="Capital_Recuperable",
                     size="Creditos_Acum", color="Universidad",
                     hover_name="Carrera_SURDAO")
    st.plotly_chart(fig, use_container_width=True)

with tab5:
    st.subheader("🔵 Bubble Empleabilidad")
    fig = px.scatter(df.head(20), x="Desercion_SIES_pct", y="Empleabilidad_%",
                     size="Capital_Recuperable", color="Universidad")
    st.plotly_chart(fig, use_container_width=True)

st.markdown("[Repo](https://github.com/TIANHH77/-Earth-Commons-DAO)")

