# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc  
**Reciprocidad > Burocracia**

> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
> — Principio materno

👉 [Dashboard en tiempo real](https://surdao-dashboard.streamlit.app/)

---

## 📊 Problema

| Año          | Ingresos | Deserción (28.8%) | Stock acumulado          |
| ------------ | -------- | ----------------- | ------------------------ |
| 2020         | 250k     | 72k               | 504k                     |
| 2021         | 250k     | 72k               | 432k                     |
| 2022         | 250k     | 72k               | 360k                     |
| **Total 7 años** | —    | —                 | ~500k estudiantes sombra |

---

## 🎯 Propósito / Purpose

- Detectar tempranamente estudiantes en riesgo (congelamiento, deserción).  
- Activar apoyos VRAE/VRA + capas comunitarias.  
- Python dashboard con datos SCT anonimizados + capas institucionales y humanas.  

---

## ⚙️ Funcionalidad (ejemplo en Python)

```python
import streamlit as st
import pandas as pd
import plotly.express as px

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

# Aplicar a dataframe
df_full["NivelAlerta"] = df_full.apply(calcular_alerta, axis=1)

st.subheader("🔔 Alertas clasificadas")
st.dataframe(df_full[["ID","Carrera","CategoriaRiesgo","EstadoBeca","ApoyoPar","CentroEstudiantes","NivelAlerta"]])
