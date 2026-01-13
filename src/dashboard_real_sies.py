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

import plotly.express as px

st.subheader("📈 Relación entre Deserción y Capital Recuperable")

# Gráfico de dispersión
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




