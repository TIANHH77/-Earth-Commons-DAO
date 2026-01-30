import streamlit as st
import pandas as pd
import plotly.express as px

# --- Configuración inicial ---
st.set_page_config(page_title="SUR DAO Dashboard", layout="wide")
st.title("🌑 SUR DAO - Custodia de Trayectorias USACH")

# --- Cargar datos reales ---
@st.cache_data
def load_real():
    df = pd.read_csv("data/surdao_real_matches_2025.csv")
    return df

df = load_real()

# --- KPIs ---
col1, col2, col3 = st.columns(3)
col1.metric("Total carreras", df.shape[0])
col2.metric("Créditos acumulados", int(df["Creditos_Acum"].sum()))
col3.metric("Capital recuperable ($MM)", round(df["Capital_Recuperable"].sum(), 2))

# --- Tabla completa ---
st.subheader("📄 Datos Reales SIES 2025")
st.dataframe(df, use_container_width=True)

# --- Gráfico de barras: impacto económico por carrera ---
fig_bar = px.bar(
    df,
    x="Carrera",
    y="Capital_Recuperable",
    color="Universidad",
    text="Capital_Recuperable",
    title="Capital humano recuperable por carrera"
)
fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
st.plotly_chart(fig_bar, use_container_width=True)

# --- Scatter: deserción vs capital recuperable ---
fig_scatter = px.scatter(
    df,
    x="Desercion_SIES_pct",
    y="Capital_Recuperable",
    color="Universidad",
    size="Creditos_Acum",
    hover_name="Carrera",
    title="Deserción vs Capital recuperable"
)
st.plotly_chart(fig_scatter, use_container_width=True)

# --- Bubble chart: deserción vs empleabilidad vs capital ---
if "Empleabilidad_%" in df.columns:
    fig_bubble = px.scatter(
        df,
        x="Desercion_SIES_pct",
        y="Empleabilidad_%",
        size="Capital_Recuperable",
        color="Universidad",
        hover_name="Carrera",
        title="Deserción vs Empleabilidad vs Capital recuperable"
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

