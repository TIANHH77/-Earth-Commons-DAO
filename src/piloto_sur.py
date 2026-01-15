import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_real_data():
    return pd.read_csv('data/surdao_real_matches_2025.csv')

st.set_page_config(page_title="SUR DAO Capa Sombra", layout="wide")
st.title("🌑 SUR DAO - Capa Sombra Dashboard")

# Datos reales SIES
df_real = load_real_data()

# Datos mock cohortes (tu piloto)
usach = pd.DataFrame({
    "ID": range(1, 101),
    "Nombre": [f"Alumno {i}" for i in range(1, 101)],
    "Carrera": ["Computación" if i % 4 == 0 else "Psicología" if i % 4 == 1 else "Construcción" if i % 4 == 2 else "Periodismo" for i in range(1, 101)],
    "Riesgo": ["Alto" if i % 3 == 0 else "Medio" if i % 3 == 1 else "Bajo" for i in range(1, 101)],
    "EstadoBeca": ["Inactivo" if i % 4 == 0 else "Activo" for i in range(1, 101)],
    "ApoyoPar": ["Sí" if i % 2 == 0 else "No" for i in range(1, 101)],
    "CreditosSCT": [60 + (i % 5) * 10 for i in range(1, 101)]
})

# Tabs Fusion
tab1, tab2 = st.tabs(["📊 SIES Real", "🔔 Cohortes Mock"])

with tab1:
    col1, col2, col3 = st.columns(3)
    col1.metric("Carreras Matches", len(df_real['carrera'].unique()))
    col2.metric("Total Créditos", f"${df_real['creditos'].sum():,.0f}MM")
    col3.metric("Deserción", f"{df_real['creditos'].sum()*0.288:,.0f}MM")
    st.dataframe(df_real)

with tab2:
    # KPIs Mock
    col1, col2, col3 = st.columns(3)
    col1.metric("Riesgo Alto", usach[usach["Riesgo"]=="Alto"].shape[0])
    col2.metric("Becas Inactivas", usach[usach["EstadoBeca"]=="Inactivo"].shape[0])
    col3.metric("Cohortes", usach.shape[0])
    
    st.subheader("🔔 Alertas Críticas")
    alertas = usach[(usach["Riesgo"].isin(["Alto", "Medio"])) & (usach["EstadoBeca"] == "Inactivo")].head(10)
    for _, row in alertas.iterrows():
        st.markdown(f"**{row['Nombre']}** – {row['Carrera']} | Riesgo: {row['Riesgo']} | Beca: {row['EstadoBeca']}")
    
    st.bar_chart(usach["Riesgo"].value_counts())
    
    # Simulación SCT
    pct = st.slider("Créditos reconvertir %", 0, 100, 60)
    reconv = usach[usach["CreditosSCT"] >= pct]
    impacto = len(reconv) * 1.5
    st.metric("Años-matrícula Recuperados", f"{impacto:.0f}")

st.markdown("---")
st.markdown("[GitHub](https://github.com/TIANHH77/-Earth-Commons-DAO) | [Ley 21.314](https://www.bcn.cl/leychile/navegar?idNorma=1186362)")

