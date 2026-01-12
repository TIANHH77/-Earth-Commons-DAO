import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# 1. Cargar datos reales
@st.cache_data
def load_data():
    return pd.read_csv("data/surdao_real_matches_2025.csv")

df = load_data()

st.title("🚀 SUR DAO Live – Datos Reales SIES 2025")
st.markdown("**USACH Fase 1: Deserción → Reconversión SCT**")

# 2. KPIs principales
col1, col2, col3, col4 = st.columns(4)
col1.metric("Carreras Alta Deserción", len(df))
col2.metric("Créditos SCT", f"{df['Creditos_Acum'].sum():,.0f}")
col3.metric("Capital Recuperable", f"${df['Capital_Recuperable'].sum():.2f}MM")
col4.metric("USACH Prioridad", "Ing. Civil Inf. + Exactas")

# 3. Tabla interactiva
st.subheader("🎯 Top Matches USACH (Deserción >35%)")
st.dataframe(
    df.style.format({
        'Capital_Recuperable': '${:.2f}MM',
        'Desercion_SIES_pct': '{:.1f}%',
        'Creditos_Acum': '{:.0f}'
    }),
    use_container_width=True
)

# 4. Gráfico de barras
st.subheader("📊 Impacto Económico por Carrera")
chart_data = df.set_index('Carrera_SURDAO')['Capital_Recuperable']
st.bar_chart(chart_data)

# 5. Recomendaciones SCT Transfer
st.subheader("🔄 Recomendaciones SCT Transfer")
for _, row in df.iterrows():
    st.success(
        f"**{row['Carrera_SURDAO']}** "
        f"({row['Desercion_SIES_pct']:.1f}% deserción) → "
        f"{int(row['SCT_Transfer_pct'])}% créditos transferibles"
    )

st.caption("Fuente: MiFuturo SIES 2025 + parser SURDAO [surdao_real_matches_2025.csv]")


