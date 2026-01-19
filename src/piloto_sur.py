import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="SUR DAO USACH", layout="wide", page_icon="🌑")
st.title("🌑 SUR DAO - Custodia de Trayectorias USACH")
st.markdown("**Datos reales SIES 2025 + USACH** | Infraestructura porosa para retención")

@st.cache_data
def load_data():
    try:
        return pd.read_csv('data/surdao_real_matches_2025.csv')
    except FileNotFoundError:
        st.warning("CSV no encontrado - usando demo")
        return pd.DataFrame({
            'carrera': ['Ing.Civil Informática C196', 'Psicología C12'],
            'desercion_pct': [40.5, 45.2],
            'creditos_sct': [208, 192],
            'impacto_mm': [2.5, 2.3]
        })

df = load_data()

# KPIs con columnas reales SOLO
col1, col2, col3 = st.columns(3)
col1.metric("Carreras Analizadas", len(df))
col2.metric("Créditos SCT Total", f"{df['creditos_sct'].sum():.0f}")
col3.metric("Impacto Humano", f"${df['impacto_mm'].sum():.1f}MM")

tab1, tab2, tab3 = st.tabs(["📊 Datos Reales SIES", "⚠️ Riesgo Alto (>40%)", "⏱️ Burocracia vs DAO"])

with tab1:
    st.subheader("Cruces SIES 2025 + Deserción USACH")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Carreras Alto Riesgo (Deserción >40%)")
    alto_riesgo = df[df['desercion_pct'] > 40]
    for _, row in alto_riesgo.iterrows():
        st.error(f"🚨 **{row['carrera']}** – {row['desercion_pct']:.1f}% – ${row['impacto_mm']:.1f}MM")

with tab3:
    st.subheader("Tiempos: Burocracia vs Custodia DAO")
    st.markdown("""
    | Fase | Burocracia | DAO Custodia | Diferencia |
    |------|------------|--------------|------------|
    | Detección | 6-12 meses | 1-2 semanas | 6x más rápido |
    | Respuesta | 3-6 meses | 1 semana | 12x más rápido |
    | Trazabilidad | Dispersa | Blockchain | 100% visible |
    """)

# Gráfico impacto
fig = px.bar(df.head(10), x='carrera', y='impacto_mm', 
             title="Impacto Humano por Carrera (Top 10)", color='desercion_pct')
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown("*SUR DAO Fase 1 - Datos SIES Mineduc 2025*")
st.markdown("[Repo](https://github.com/TIANHH77/-Earth-Commons-DAO)")