import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SUR DAO Dashboard", layout="wide")
st.title("🌑 SUR DAO - Capa Sombra Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("data/surdao_real_matches_2025.csv")

df = load_data()

# --- Pestañas principales ---
tab1, tab2, tab3, tab4 = st.tabs(["📊 KPIs", "📄 Tabla", "📊 Barras", "📈 Scatter"])

# --- KPIs ---
with tab1:
    st.subheader("📊 Indicadores clave")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total carreras SURDAO", df.shape[0])
    col2.metric("Créditos acumulados", int(df["Creditos_Acum"].sum()))
    col3.metric("Capital recuperable ($MM)", round(df["Capital_Recuperable"].sum(), 2))

# --- Tabla interactiva ---
with tab2:
    st.subheader("📄 Matches SURDAO-SIES")
    st.dataframe(df, use_container_width=True)

# --- Gráfico de barras ---
with tab3:
    st.subheader("📊 Impacto Económico por Carrera (Capital Recuperable)")
    fig_bar = px.bar(
        df,
        x="Carrera_SURDAO",
        y="Capital_Recuperable",
        color="Universidad",
        text="Capital_Recuperable",
        labels={"Carrera_SURDAO": "Carrera", "Capital_Recuperable": "Capital Recuperable ($MM)"},
        title="Capital humano recuperable por carrera"
    )
    fig_bar.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig_bar.update_layout(
        xaxis_title="Carrera",
        yaxis_title="Capital Recuperable ($MM)",
        uniformtext_minsize=8,
        uniformtext_mode='hide'
    )
    st.plotly_chart(fig_bar, use_container_width=True)

# --- Scatter plot ---
with tab4:
    st.subheader("📈 Relación entre Deserción y Capital Recuperable")
    fig_scatter = px.scatter(
        df,
        x="Desercion_SIES_pct",
        y="Capital_Recuperable",
        color="Universidad",
        size="Creditos_Acum",
        hover_name="Carrera_SURDAO",
        labels={
            "Desercion_SIES_pct": "Tasa de Deserción (%)",
            "Capital_Recuperable": "Capital Recuperable ($MM)"
        },
        title="Relación entre tasa de deserción y capital recuperable por carrera"
    )
    fig_scatter.update_traces(marker=dict(opacity=0.7, line=dict(width=1, color='DarkSlateGrey')))
    fig_scatter.update_layout(
        xaxis_title="Tasa de Deserción (%)",
        yaxis_title="Capital Recuperable ($MM)",
        legend_title="Universidad"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)





