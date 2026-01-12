import streamlit as st
import pandas as pd

st.title("🌑 SUR DAO - Capa Sombra Dashboard")

# --- Datos mock para que siempre levante ---
usach = pd.DataFrame({
    "ID": range(1, 101),
    "Nombre": [f"Alumno {i}" for i in range(1, 101)],
    "Riesgo": ["Alto" if i % 3 == 0 else "Medio" if i % 3 == 1 else "Bajo" for i in range(1, 101)],
    "EstadoBeca": ["Inactivo" if i % 4 == 0 else "Activo" for i in range(1, 101)],
    "ApoyoPar": ["Sí" if i % 2 == 0 else "No" for i in range(1, 101)],
    "CentroEstudiantes": ["Activo" if i % 5 != 0 else "Inactivo" for i in range(1, 101)],
})

st.subheader("🧑‍🎓 Cohorte USACH (mock)")
st.dataframe(usach.head(20))

st.subheader("🔔 Alertas combinadas (demo)")
alertas = usach[
    (usach["Riesgo"].isin(["Alto", "Medio"])) &
    (usach["EstadoBeca"] == "Inactivo")
]

for _, row in alertas.head(10).iterrows():
    st.markdown(f"""
        **Estudiante {row['ID']} ({row['Nombre']})** – {row['Riesgo']} → 
        Sin beca ministerial, Apoyo par: {row['ApoyoPar']}, 
        Centro estudiantes: {row['CentroEstudiantes']}
    """)



