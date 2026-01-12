<<<<<<< HEAD
 "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste." +— 

Principio materno, SUR DAO+# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc +**Reciprocidad > Burocracia**
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
+++python import numpy as np
=======
# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc

> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
> — Principio materno.

**Reciprocidad > Burocracia**

Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

👉 [Dashboard en tiempo real](https://surdao-dashboard.streamlit.app/)

## 📊 Problema

| Año         | Ingresos | Deserción (28.8%) | Stock acumulado       |
|-------------|----------|-------------------|-----------------------|
| 2020        | 250k     | 72k               | 504k                  |
| 2021        | 250k     | 72k               | 432k                  |
| 2022        | 250k     | 72k               | 360k                  |
| **Total 7 años** | —     | —                 | ~500k estudiantes sombra |

**Fuente:** Mineduc/SIES (28.8% primer año)[web:10][web:13]

## 🎯 Propósito
- Detectar tempranamente estudiantes en riesgo (congelamiento, deserción).
- Activar apoyos VRAE/VRA + capas comunitarias.
- Python dashboard con datos SCT anonimizados + capas institucionales/humanas.

## ⚙️ Funcionalidad

```python
import streamlit as st
import pandas as pd
>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa

def calcular_alerta(row):
    riesgo = row["CategoriaRiesgo"]
    beca = row.get("EstadoBeca", "Inactivo")
    apoyo_par = row.get("ApoyoPar", "No")
    centro = row.get("CentroEstudiantes", "Inactivo")
<<<<<<< HEAD

=======
    
>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa
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

<<<<<<< HEAD
df_full["NivelAlerta"] = df_full.apply(calcular_alerta, axis=1)

st.subheader("🔔 Alertas clasificadas")
st.dataframe(df_full[["ID","Carrera","CategoriaRiesgo","EstadoBeca","ApoyoPar","CentroEstudiantes","NivelAlerta"]])

📊 Distribución de NivelAlerta
+++python import plotly.express as px

df_counts = df_full["NivelAlerta"].value_counts().reset_index()
df_counts.columns = ["NivelAlerta", "Cantidad"]

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

🔔 Ejemplos de alertas del piloto

|ID	|Carrera	|Riesgo	|Beca	|Apoyo |Par	|Centro |Estudiantes	|Alerta |generada
|1	|Arquitectura	|Medio	|Inactivo	|No	|Inactivo	|Sin beca ministerial
|2	|Derecho	|Medio	|Inactivo	|Sí	|Activo	|Sin beca + |Apoyo pares + |Centro activo
|4	|Derecho	|Alto	|Inactivo	|Sí	|Inactivo	|Riesgo alto + |Sin beca + |Apoyo pares

Lógica: Riesgo crítico = medio/alto + sin beca + sin pares + sin centro. Se prioriza acompañamiento donde hay red activa, pero falta cobertura estatal.

+++mermaid 
=======
# Ejemplo uso
df_full["NivelAlerta"] = df_full.apply(calcular_alerta, axis=1)
st.subheader("🔔 Alertas clasificadas")
st.dataframe(df_full[["ID","Carrera","CategoriaRiesgo","EstadoBeca","ApoyoPar","CentroEstudiantes","NivelAlerta"]])

| ID | Carrera      | Riesgo | Beca     | Apoyo Par | Centro   | Alerta Final              |
| -- | ------------ | ------ | -------- | --------- | -------- | ------------------------- |
| 1  | Arquitectura | Medio  | Inactivo | No        | Inactivo | 🔴 Riesgo crítico         |
| 2  | Derecho      | Medio  | Inactivo | Sí        | Activo   | 🟠 Riesgo con red parcial |
| 4  | Derecho      | Alto   | Inactivo | Sí        | Inactivo | 🟠 Riesgo con red parcial |
Lógica: Riesgo crítico = medio/alto + sin beca + sin pares + sin centro.

🏗️ Arquitectura
>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]

<<<<<<< HEAD

📊 Datos clave
28.8% tasa de deserción en primer año (SIES).

427 renuncias en USACH durante 2022.

14.6% deserción permanente (OECD).

Falta de coordinación entre MINEDUC, JUNAEB, becas internas y apoyo comunitario.

🧠 IA Entrenamiento SUR DAO
+++python
# src/ml_train.py
=======
📊 Datos Clave
28.8% deserción primer año (SIES).[web:10]
427 renuncias USACH 2022.[web:23]
14.6% deserción permanente (OECD).[web:18]
Falta coordinación MINEDUC/JUNAEB/becas/apoyo comunitario.

🧠 IA: src/ml_train.py
>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

usach = pd.DataFrame({
    'nota': [7.0 + i/10 for i in range(100)],
    'riesgo': ['alto' if i%3==0 else 'medio' for i in range(100)]
})
<<<<<<< HEAD

X = usach[['nota']]
y = usach['riesgo']

=======
X = usach[['nota']]
y = usach['riesgo']
>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)


<<<<<<< HEAD
=======







>>>>>>> 14704049c1495aa85cba3349ba4bbb95267cdcaa
