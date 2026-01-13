import streamlit as st
import pandas as pd
import plotly.express as px   # 👈 aquí importas Plotly

st.title("🌑 SUR DAO - Dashboard SIES 2025")

@st.cache_data
def load_data():
    return pd.read_csv("data/surdao_real_matches_2025.csv")

df = load_data()

# --- KPIs principales ---
st.subheader("📊 Indicadores clave")
st.metric("Total carreras SURDAO", df.shape[0])
st.metric("Créditos acumulados", df["Creditos_Acum"].sum())
st.metric("Capital recuperable ($MM)", df["Capital_Recuperable"].sum())

# --- Tabla interactiva ---
st.subheader("📄 Tabla de Matches SURDAO-SIES")
st.dataframe(df)

# --- Gráfico Plotly (impacto económico por carrera) ---
st.subheader("📊 Impacto Económico por Carrera (Capital Recuperable)")
fig = px.bar(
    df,
    x="Carrera_SURDAO",
    y="Capital_Recuperable",
    color="Universidad",
    text="Capital_Recuperable",
    labels={"Carrera_SURDAO": "Carrera", "Capital_Recuperable": "Capital Recuperable ($MM)"},
    title="Capital humano recuperable por carrera"
)
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_layout(
    xaxis_title="Carrera",
    yaxis_title="Capital Recuperable ($MM)",
    uniformtext_minsize=8,
    uniformtext_mode='hide'
)
st.plotly_chart(fig, use_container_width=True)



