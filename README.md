# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc

> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
> — Principio materno

**Reciprocidad > Burocracia**

Detecta estudiantes **"sombra"** (congelados con créditos) → **trueque/recuperación** → ROI nacional.

👉 [![SUR DAO Live](https://img.shields.io/badge/Streamlit-LIVE-brightgreen)](https://surdao-dashboard.streamlit.app/)

## 📊 Problema: 500k Estudiantes Sombra

| Año          | Ingresos | Deserción 28.8% | Stock Acumulado     |
|:-------------|:---------|:----------------|:--------------------|
| 2020         | 250k     | 72k             | 504k                |
| 2021         | 250k     | 72k             | 432k                |
| 2022         | 250k     | 72k             | 360k                |
| **Total**    | **—**    | **—**           | **~500k sombra**    |

**[SIES/Mineduc]** [web:10]

## 🎓 **NUEVO:** Capital Humano RESCATABLE

| Estudiante        | Porcentaje_Carrera | Años_Estudiados | Valor_Invertido_MCLP | SUR_DAO_Recupera           |
|:------------------|:-------------------|:----------------|:---------------------|:---------------------------|
| Pepito Derecho    | 62%                | 3.5             | $17.5M               | ✅ Trueque créditos         |
| Juan Arquitectura | 45%                | 2               | $10M                 | ✅ Reingreso sin penalidad  |
| Total 500k sombra | ~50%               | 2.5 promedio    | **$6 billones**      | ✅ ROI nacional             | [code_file:0]

**No "desertores" – ASSETs latentes $6 billones!**

## 🎯 Propósito
SCT datos → % créditos completados → Trueque DAO → Reingreso
Pepito 62% Derecho NO empieza cero → termina en 1.5 años


## ⚙️ Motor Reglas

```python
def calcular_alerta(row):
    riesgo = row["CategoriaRiesgo"]
    %creditos = row["PorcentajeCarrera"]  # NUEVO
    beca = row.get("EstadoBeca", "Inactivo")
    
    if %creditos > 50 and beca == "Inactivo":
        return "🟡 Créditos rescatables (trueque DAO)"
    # ... resto lógica original

🔔 Ejemplos Prácticos

| ID | Carrera      | % Carrera | Alerta SUR DAO       |
| -- | ------------ | --------- | -------------------- |
| 1  | Arquitectura | 62%       | 🔴 Trueque créditos  |
| 2  | Derecho      | 45%       | 🟠 Reingreso + pares |

🏗️ Arquitectura Trueque
flowchart TD
  A[Datos SCT + % créditos] --> B[Motor reglas Python]
  B --> C[Dashboard VRA + Trueque]
  C --> D[Alertas "créditos rescatables"]
  D --> E[MINEDUC valida → Becas]
  E --> F[DAO pares trueque créditos]

💰 Impacto Cuantificado
500k x 50% carrera x $5M/año = $6 billones capital humano
SUR DAO 20% recuperación = $1.2 billones ROI anual


