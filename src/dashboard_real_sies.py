import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Datos reales ejecutados [code_file:33]
@st.cache_data
def load_real_data():
    return pd.read_csv('surdao_real_matches_2025.csv')

df = load_real_data()

st.title("🚀 SUR DAO Live - Datos REALES SIES 2025")
st.markdown("**USACH Fase 1: Deserción → Reconversión SCT**")

# KPIs fila 1
col1, col2, col3, col4 = st.columns(4)
col1.metric("Carreras Alta Deserción", len(df))
col2.metric("Créditos SCT", f"{df['Creditos_Acum'].sum():,.0f}")
col3.metric("Capital Recuperable", f"${df['Capital_Recuperable'].sum():.1f}MM")
col4.metric("USACH Prioridad", "Ing. Civil Inf. + Exactas")

# Tabla interactiva
st.subheader("🎯 Top Matches USACH (Deserción >35%)")
st.dataframe(df.style.format({'Capital_Recuperable': '${:.2f}MM'}), use_container_width=True)

# Gráfico barras
st.subheader("📊 Impacto Económico")
chart_data = df.set_index('Carrera')['Capital_Recuperable']
st.bar_chart(chart_data)

# Match recomendaciones
st.subheader("🔄 Recomendaciones SCT Transfer")
for idx, row in df.iterrows():
    st.success(f"**{row['Carrera']}** ({row['Desercion_SIES_pct']:.1f}% deserción) → {int(row['SCT_Transfer_pct'])}% créditos transferibles")

st.caption("Fuente: MiFuturo SIES 2025 + deserción histórica [file:26][code_file:33]")
