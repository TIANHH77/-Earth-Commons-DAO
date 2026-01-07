# SUR DAO – Earth Commons DAO (USACH Pilot)

**Piloto SUR DAO – Herramienta de Monitoreo Integral de Estudiantes USACH**  
Early detection of dropout risk using anonymized data. No regulations changed.  

[![Streamlit Demo](https://streamlit.io/images/brand/streamlit-logo-primary-colormark-lighttext.png)](https://streamlit.io)

---

## 🎯 Propósito / Purpose
Detectar tempranamente estudiantes en riesgo (congelamiento, deserción) → activar apoyos VRAE/VRA.  
Python dashboard con datos SCT anonimizados.  
📄 Documentación completa: [`docs/piloto_piloto.md`](docs/piloto_piloto.md)

---

## 📊 Problem
- **28.8%** tasa de deserción en primer año (SIES).  
- **427 renuncias** en USACH durante 2022.  
- Falta un sistema integrado que conecte datos académicos con apoyos psicosociales.  

---

## 🛠️ Arquitectura del piloto
```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]

