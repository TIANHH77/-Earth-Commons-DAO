"El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste." +— Principio materno. 

SUR DAO+# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc +**Reciprocidad > -Burocracia**
+Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

👉 Dashboard en tiempo real
[![Streamlit](https://surdao-dashboard.streamlit.app/)]


📊 Problema

| Año          | Ingresos | Deserción (28.8%) | Stock acumulado          |
| ------------ | -------- | ----------------- | ------------------------ |
| 2020         | 250k     | 72k               | 504k                     |
| 2021         | 250k     | 72k               | 432k                     |
| 2022         | 250k     | 72k               | 360k                     |
| Total 7 años | —        | —                 | ~500k estudiantes sombra |


🎯 Propósito / Purpose
Detectar tempranamente estudiantes en riesgo (congelamiento, deserción).

Activar apoyos VRAE/VRA + capas comunitarias.

Python dashboard con datos SCT anonimizados + capas institucionales y humanas.

⚙️ Funcionalidad (ejemplo en Python)

import streamlit as st
import pandas as pd

def calcular_alerta(row):
    riesgo = row["CategoriaRiesgo"]
    beca = row.get("EstadoBeca", "Inactivo")
    apoyo_par = row.get("ApoyoPar", "No")
    centro = row.get("CentroEstudiantes", "Inactivo")
    
    if "Sin riesgo" in riesgo:
        return "🟢 Sin riesgo"
    if "Riesgo leve" in riesgo:
        return "🟡 Riesgo leve"
    if "Riesgo medio" in riesgo or "Riesgo alto" in riesgo:
        if beca == "Inactivo" and apoyo_par == "No" and centro == "Inactivo":
            return "🔴 Riesgo crítico (aislamiento total)"
        else:
            return "🟠 Riesgo con red parcial"
    return "⚪ No clasificado"

# Ejemplo uso
df_full["NivelAlerta"] = df_full.apply(calcular_alerta, axis=1)
st.subheader("🔔 Alertas clasificadas")
st.dataframe(df_full[["ID","Carrera","CategoriaRiesgo","EstadoBeca","ApoyoPar","CentroEstudiantes","NivelAlerta"]])


🔔 Ejemplos de alertas del piloto

| ID | Carrera      | Riesgo | Beca     | Apoyo Par | Centro   | Alerta Final              |
| -- | ------------ | ------ | -------- | --------- | -------- | ------------------------- |
| 1  | Arquitectura | Medio  | Inactivo | No        | Inactivo | 🔴 Riesgo crítico         |
| 2  | Derecho      | Medio  | Inactivo | Sí        | Activo   | 🟠 Riesgo con red parcial |
| 4  | Derecho      | Alto   | Inactivo | Sí        | Inactivo | 🟠 Riesgo con red parcial |

Lógica: Riesgo crítico = medio/alto + sin beca + sin pares + sin centro. Se prioriza acompañamiento donde hay red activa, pero falta cobertura estatal.

+++mermaid 
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]



📊 Datos clave
28.8% tasa de deserción en primer año (SIES).

427 renuncias en USACH durante 2022.

14.6% deserción permanente (OECD).

Falta de coordinación entre MINEDUC, JUNAEB, becas internas y apoyo comunitario.

🧠 IA Entrenamiento SUR DAO
+++python
# src/ml_train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

usach = pd.DataFrame({
    'nota': [7.0 + i/10 for i in range(100)],
    'riesgo': ['alto' if i%3==0 else 'medio' for i in range(100)]
})

X = usach[['nota']]
y = usach['riesgo']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)


