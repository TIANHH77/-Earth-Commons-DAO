 "SUR DAO = Universidades ganan $1.2B matrícula + MINEDUC cumple metas + estudiantes títulos sin deuda."

# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc  
**Reciprocidad > Burocracia**  
**Trayectorias Flexibles DAO**

👉 [![SUR DAO Live](https://img.shields.io/badge/Streamlit-LIVE-brightgreen)](https://surdao-dashboard.streamlit.app/)

---

## 📊 Crisis: 500k Estudiantes Sombra
- **28.8%** deserción en primer año (SIES).  
- **500k créditos vigentes** acumulados en estudiantes que abandonaron.  
- **Capital humano latente estimado: $6B**.  

---

## 🎯 Propósito
- Detectar tempranamente estudiantes en riesgo.  
- Reconectar trayectorias congeladas o abandonadas.  
- Reconversión inteligente de créditos SCT hacia áreas críticas.  
- Activar apoyos institucionales (MINEDUC, JUNAEB, VRAE/VRA) y comunitarios (pares, centros de estudiantes).  

---

## 🔄 Match Deserción → Afines Prioritarios
Ejemplos de reconversión:  

| Carrera origen     | Tasa deserción | Destino afín prioritario     | % Créditos SCT |
|:-------------------|:---------------|:-----------------------------|:---------------|
| Ing. Computación   | 40.5%          | Automatización Industrial A  | **75%**        |
| Ciencias Exactas   | 59.5%          | Ing. Civil + Pedagogía A/B   | **60%**        |
| Técnico Construcción | 40%          | Ing. Civil Construcción A    | **80%**        |
| Logística          | 35%            | Gestión Pública A            | **65%**        |

| Actor         | Problema Actual             | SUR DAO Solución              | Ganancia $ Anual |
|:--------------|:----------------------------|:------------------------------|:-----------------|
| **MINEDUC**   | **76% retención** meta FES | **+20% reingresos**           | **+$500B**       |
| **Universidades** | **-15% matrícula** gratuidad | **80% créditos** → nueva matrícula | **+$1.2B** |
| **Estudiante**| **Deuda + 0 créditos**      | **Trueque 1.5 años** → título | **Sin deuda**   |
| **SENCE**     | **Déficit técnicos**        | **Match deserción → Automatización** | **85% empleo** |

**Ley 21.091 Art.28:** SCT convalidación **OBLIGATORIA** [web:78]
**Negocio UES:** 500k sombra x 20% recuperación = **100k nueva matrícula** → **millones ingresos gratuidad**.
**Filosofía:** Los créditos **no se pierden** → se **reconvierten inteligentemente**.  

---
```python
def winwin_ues(match):
    if match["ley_21091"] and match["pct_sct"] > 60:
        return "💰 UES: Nueva matrícula + MINEDUC: Retención"
    return "Revisar convalidación"



## 📊 Mapa de Oportunidades
🔴Zona Crítica: Psicología/Periodismo (deserción + saturación)
🟢 Zona Oportunidad: Computación/Construcción (deserción alta → demanda)

---
**SUR DAO dirige trueque inteligente.**
## 🏗️ Arquitectura SUR DAO

```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]






