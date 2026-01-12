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

