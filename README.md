> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
— Principio materno, SUR DAO

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

| Riesgo académico | Beneficios institucionales       | Apoyo entre pares | Centro de estudiantes | Planteamiento sugerido                                      |
|------------------|----------------------------------|--------------------|------------------------|--------------------------------------------------------------|
| 🔴 Alto          | ❌ Sin beca ministerial/JUNAEB   | ❌ No apoyo par    | ❌ Inactivo            | Derivación urgente a VRAE + ONG psicosocial                  |
| 🔴 Alto          | ❌ Sin beca ministerial          | ✅ Apoyo par       | ✅ Activo              | Contención grupal + asesoría administrativa                  |
| 🟠 Medio         | ✅ Becas activas                 | ✅ Apoyo par       | ❌ Inactivo            | Seguimiento académico + mentoría estudiantil                 |
| 🟡 Leve          | ✅ Becas activas                 | ❌ No apoyo par    | ✅ Activo              | Tutorías comunitarias + monitoreo ligero                     |
| 🟢 Sin riesgo    | ✅ Becas activas                 | ✅ Apoyo par       | ✅ Activo              | Mantener acompañamiento, reforzar comunidad                  |




