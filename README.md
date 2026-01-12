+> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste." +— 

Principio materno, SUR DAO+# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc +**Reciprocidad > Burocracia**
+Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

👉 Dashboard en tiempo real
[![Streamlit](https://surdao-dashboard.streamlit.app/)]

## 📊 Problema
| Año | Ingresos | Deserción | Stock |
|-----|----------|-----------|-------|
| 2020| 250k    | 72k      | 504k |
**Total**: ~500k sombra

+---
+## 📊 Problema: 71k anual → 500k+ sombra acumulada + +| Año | Ingresos | Deserción (28.8%) | Stock acumulado | +|------|----------|-------------------|-----------------| +| 2020 | 250k | 72k | 504k | +| 2021 | 250k | 72k | 432k | +| 2022 | 250k | 72k | 360k | +| **Total 7 años** | — | — | ~500k estudiantes sombra | + +**Fuente:** Mineduc/SIES (28.8% primer año) + USACH Anuario (14.6% reprobación)
+--- + +## ⚙️ Funcionalidad (ejemplo en Python)import numpy as np

def calcular_alerta(row):
    riesgo = row["CategoriaRiesgo"]
    beca = row.get("EstadoBeca", "Inactivo")
    apoyo_par = row.get("ApoyoPar", "No")
    centro = row.get("CentroEstudiantes", "Inactivo")

    # Caso sin riesgo
    if "Sin riesgo" in riesgo:
        return "🟢 Sin riesgo"

    # Riesgo leve
    if "Riesgo leve" in riesgo:
        return "🟡 Riesgo leve"

    # Riesgo medio/alto
    if "Riesgo medio" in riesgo or "Riesgo alto" in riesgo:
        # Riesgo crítico: sin beca + sin pares + sin centro
        if beca == "Inactivo" and apoyo_par == "No" and centro == "Inactivo":
            return "🔴 Riesgo crítico (aislamiento total)"
        # Riesgo alto/medio con alguna red activa
        else:
            return "🟠 Riesgo con red parcial"

    return "⚪ No clasificado"

# Aplicar al dataframe
df_full["NivelAlerta"] = df_full.apply(calcular_alerta, axis=1)

# Mostrar ejemplo
st.subheader("🔔 Alertas clasificadas")
st.dataframe(df_full[["ID","Carrera","CategoriaRiesgo","EstadoBeca","ApoyoPar","CentroEstudiantes","NivelAlerta"]])

import plotly.express as px

st.subheader("📊 Distribución de NivelAlerta")

# Contar estudiantes por categoría
df_counts = df_full["NivelAlerta"].value_counts().reset_index()
df_counts.columns = ["NivelAlerta", "Cantidad"]

# Gráfico de torta
fig_pie = px.pie(
    df_counts,
    names="NivelAlerta",
    values="Cantidad",
    color="NivelAlerta",
    title="Proporción de estudiantes por nivel de alerta",
    hole=0.3
)

fig_pie.update_traces(textinfo="percent+label")
st.plotly_chart(fig_pie, use_container_width=True)

## 📊 Problema


[Tu tabla 71k-500k]

## 🛠️ Arquitectura
```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor reglas Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[MINEDUC/JUNAEB/Becas]
  E --> F[Apoyo pares/centro]
+---
## 🎯 Propósito / Purpose
+Detectar tempranamente estudiantes en riesgo (congelamiento, deserción) → activar apoyos VRAE/VRA. +Python dashboard con datos SCT anonimizados + capas institucionales y comunitarias. ---
## 📊 Datos clave
+- **28.8%** tasa de deserción en primer año (SIES). +- **427 renuncias** en USACH durante 2022. +- **14.6%** deserción permanente (OECD). +- Falta de coordinación entre MINEDUC, JUNAEB, becas internas y apoyo comunitario. ---
## 🔔 Alertas combinadas (ejemplos del piloto)
+| ID | Carrera | Riesgo | Beca | Apoyo Par | Centro Estudiantes | Alerta generada | +|----|--------------|--------|----------|-----------|--------------------|-----------------| +| 1 | Arquitectura | Medio | Inactivo | No | Inactivo | Sin beca ministerial | +| 2 | Derecho | Medio | Inactivo | Sí | Activo | Sin beca + Apoyo pares + Centro activo | +| 4 | Derecho | Alto | Inactivo | Sí | Inactivo | Riesgo alto + Sin beca + Apoyo pares | **Lógica**: Alertas solo para Riesgo medio/alto + Sin beca ministerial. Se prioriza acompañamiento donde hay red activa (pares/centro) pero falta cobertura estatal. ---

## 🛠️ Arquitectura del piloto

+```mermaid +flowchart TD + A[Datos SCT anon.] --> B[Motor de reglas en Python] + B --> C[Dashboard VRA/VRAE] + C --> D[Alertas psicosociales] + D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas] + E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes] +

## 🧠 IA Entrenamiento SUR DAO

```python
# src/ml_train.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Tu data mock
usach = pd.DataFrame({
    'nota': [7.0 + i/10 for



