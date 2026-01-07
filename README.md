# SUR DAO – Earth Commons DAO (USACH Pilot)

**Piloto SUR DAO – Herramienta de Monitoreo Integral de Estudiantes USACH**  
Early detection of dropout risk using anonymized data. No regulations changed.  

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://<tu-usuario>-earth-commons-dao.streamlit.app)

---

## 🎯 Propósito / Purpose
Detectar tempranamente estudiantes en riesgo (congelamiento, deserción) → activar apoyos VRAE/VRA.  
Python dashboard con datos SCT anonimizados + capas institucionales y comunitarias.  
📄 Documentación completa: [`docs/piloto_piloto.md`](docs/piloto_piloto.md)

---



## 📊 Problem
- **28.8%** tasa de deserción en primer año (SIES).  
- **427 renuncias** en USACH durante 2022.  
- **14.6%** deserción permanente (OECD).  
- Falta de coordinación entre MINEDUC, JUNAEB, becas internas y apoyo comunitario.  

---

## 🛠️ Arquitectura del piloto
```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]




## 📜 Segundo Manifiesto SUR DAO
- La deserción no es solo estadística: es 71k estudiantes/año invisibilizados en la capa sombra.
- Cada combinación de riesgo + beneficios + apoyo humano activa un planteamiento concreto.
- El SUR DAO integra datos y comunidad: pares, centros de estudiantes, ONG psicosociales.
- Reciprocidad > Burocracia: el código abierto es herramienta + espíritu liberados.
- Este piloto no es un tablero: es un manifiesto vivo de cómo debería funcionar la educación superior.



