# 🌑 SUR DAO – Earth Commons DAO (USACH Pilot)

**Piloto SUR DAO – Herramienta de Monitoreo Estudiantes USACH**  
*Early detection of dropout risk using anonymized data. No regulations changed.*

[![Streamlit Demo](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sur-dao-piloto.streamlit.app)

## 🎯 Propósito / Purpose
Detecta estudiantes en riesgo (congelamiento, deserción) → activa apoyos VRAE/VRA. Python dashboard con datos SCT anonimizados. [docs/piloto.md]

**Problem**: 28.8% dropout año 1 (SIES). USACH 427 renuncias 2022. [web:36]

## 🏗️ Arquitectura
```mermaid
graph TD
  A[Datos SCT anon.] --> B[Reglas Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
