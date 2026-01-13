import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/surdao_real_matches_2025.csv")
    # Añadir columna si falta (MiFuturo cross)
    if 'Empleabilidad_%' not in df.columns:
        df['Empleabilidad_%'] = 85.0  # Default
    return df

df = load_data()

# ✅ TABS CORRECTOS con WITH
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 KPIs", "📄 Tabla", "📊 Barras", 
    "📈 Scatter", "🔵 Bubble Chart"
])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Estudiantes USACH", "274")
    col2.metric("Créditos SCT", "42,480")
    col3.metric("Impacto $MM", "509")

with tab2:
    st.dataframe(df)

with tab5:  # Bubble Chart ✅
    st.subheader("🔵 Deserción vs Empleabilidad vs Capital")
    fig_bubble = px.scatter(
        df, x="Desercion_pct", y="Empleabilidad_%", 
        size="Valor_MM", color="Afin",
        hover_name="Carrera", title="SURDAO Matches Fase 1",
        labels={"Desercion_pct": "Deserción %", "Valor_MM": "$MM"}
    )
    fig_bubble.update_traces(marker=dict(opacity=0.7))
    st.plotly_chart(fig_bubble, use_container_width=True)





