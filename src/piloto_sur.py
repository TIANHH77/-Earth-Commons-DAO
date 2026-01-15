import streamlit as st
import pandas as pd

st.title("🌑 SUR DAO - Capa Sombra Dashboard")

# --- Datos mock para demo funcional ---
usach = pd.DataFrame({
    "ID": range(1, 101),
    "Nombre": [f"Alumno {i}" for i in range(1, 101)],
    "Carrera": ["Computación" if i % 4 == 0 else "Psicología" if i % 4 == 1 else "Construcción" if i % 4 == 2 else "Periodismo" for i in range(1, 101)],
    "Riesgo": ["Alto" if i % 3 == 0 else "Medio" if i % 3 == 1 else "Bajo" for i in range(1, 101)],
    "EstadoBeca": ["Inactivo" if i % 4 == 0 else "Activo" for i in range(1, 101)],
    "ApoyoPar": ["Sí" if i % 2 == 0 else "No" for i in range(1, 101)],
    "CreditosSCT": [60 + (i % 5) * 10 for i in range(1, 101)],  # créditos acumulados
})

# --- KPIs principales ---
st.subheader("📊 Indicadores clave")
st.metric("Estudiantes en riesgo alto", usach[usach["Riesgo"]=="Alto"].shape[0])
st.metric("Becas inactivas", usach[usach["EstadoBeca"]=="Inactivo"].shape[0])
st.metric("Total cohortes", usach.shape[0])

# --- Cohorte completa (vista rápida) ---
st.subheader("🧑‍🎓 Cohorte USACH (mock)")
st.dataframe(usach.head(20))

# --- Alertas combinadas ---
st.subheader("🔔 Alertas críticas")
alertas = usach[
    (usach["Riesgo"].isin(["Alto", "Medio"])) &
    (usach["EstadoBeca"] == "Inactivo")
]

for _, row in alertas.head(10).iterrows():
    st.markdown(f"""
        **{row['Nombre']}** – {row['Carrera']}  
        Riesgo: {row['Riesgo']} | Beca: {row['EstadoBeca']} | Apoyo par: {row['ApoyoPar']}
    """)

# --- Distribución de riesgo ---
st.subheader("📊 Distribución de Riesgo")
st.bar_chart(usach["Riesgo"].value_counts())

# --- Mapa de oportunidades ---
st.subheader("🗺️ Mapa de Oportunidades")
st.markdown("""
- 🔴 **Zona Crítica:** Psicología / Periodismo (deserción + saturación)  
- 🟢 **Zona Oportunidad:** Computación / Construcción (deserción alta → demanda)  
""")

# --- Simulación de reconversión de créditos SCT ---
st.subheader("🔄 Simulación de Reconversión de Créditos SCT")

# Slider para elegir % de créditos a reconvertir
pct_reconversion = st.slider("Porcentaje de créditos a reconvertir", 0, 100, 60)

# Filtrar estudiantes con créditos suficientes
reconvertidos = usach[usach["CreditosSCT"] >= pct_reconversion]

st.write(f"Estudiantes con ≥ {pct_reconversion}% créditos SCT disponibles para reconversión: {reconvertidos.shape[0]}")

# Mostrar algunos casos
st.dataframe(reconvertidos[["Nombre", "Carrera", "CreditosSCT"]].head(10))

# KPI de impacto estimado
impacto = reconvertidos.shape[0] * 1.5  # ejemplo: cada reconversión equivale a 1.5 años de matrícula recuperada
st.metric("Impacto estimado en años-matrícula recuperados", impacto)


import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_real_data():
    return pd.read_csv('data/surdao_real_matches_2025.csv')

st.set_page_config(page_title="SUR DAO Capa Sombra", layout="wide")

st.title("🌑 SUR DAO - Capa Sombra Dashboard")

# KPIs Macro (Datos reales)
df = load_real_data()
col1, col2, col3 = st.columns(3)
col1.metric("Carreras Matches", len(df['carrera'].unique()))
col2.metric("Total Créditos", f"${df['creditos'].sum():,.0f}MM")
col3.metric("Deserción Est.", f"{df['creditos'].sum()*0.288:,.0f}MM")

# Tabla SIES Real (Tab 1)
tab1, tab2 = st.tabs(["📊 SIES Matches", "🔔 Alertas Capa Sombra"])

with tab1:
    st.subheader("Matches SURDAO-SIES")
    st.dataframe(df, use_container_width=True)

with tab2:
    # KPIs Mock → Real
    st.subheader("📊 Indicadores Clave")
    col1, col2, col3 = st.columns(3)
    col1.metric("Estudiantes Riesgo Alto", int(len(df)*0.33))
    col2.metric("Becas Inactivas", int(len(df)*0.25))
    col3.metric("Cohortes Total", 100)
    
    # Alertas Críticas (Simuladas → reales)
    st.subheader("🔔 Alertas Críticas")
    risky = df.sample(10).copy()
    risky['riesgo'] = ['Alto' if i%2 else 'Medio' for i in range(10)]
    risky['beca'] = 'Inactiva'
    st.dataframe(risky[['carrera', 'riesgo', 'beca']], use_container_width=True)
    
    # Gráficos
    fig = px.bar(df, x='carrera', y='creditos', title="Distribución Riesgo")
    st.plotly_chart(fig)
    
    # Simulación SCT
    pct = st.slider("Créditos reconvertir %", 0, 100, 60)
    impacto = df['creditos'].sum() * pct/100 * 1.5
    st.metric("Años-matrícula Recuperados", f"{impacto:.0f}")

st.markdown("---")
st.markdown("[GitHub Repo](https://github.com/TIANHH77/-Earth-Commons-DAO) | [Ley 21.314 Convalidación](https://www.bcn.cl/leychile/navegar?idNorma=1186362)")


