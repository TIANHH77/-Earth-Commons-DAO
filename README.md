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

### Alertas combinadas (resumen)

La app genera alertas solo para estudiantes en **Riesgo medio** o **Riesgo alto**, combinando becas, apoyo entre pares y centros de estudiantes activos:

### Alertas combinadas (ejemplos reales del piloto)
En la app, cada fila se muestra como:  

| ID | Carrera       | Categoría Riesgo | Beca     | Apoyo Par | Centro Estudiantes | Alerta generada |
|----|---------------|------------------|----------|-----------|--------------------|-----------------|
| 1  | Arquitectura  | Riesgo medio     | Inactivo | No        | Inactivo           | **Estudiante 1 (Arquitectura)** – Riesgo medio → Sin beca ministerial |
| 2  | Derecho       | Riesgo medio     | Inactivo | Sí        | Activo             | **Estudiante 2 (Derecho)** – Riesgo medio → Sin beca ministerial, Apoyo entre pares activo, Centro de estudiantes activo |
| 3  | Psicología    | Riesgo medio     | Inactivo | Sí        | Inactivo           | **Estudiante 3 (Psicología)** – Riesgo medio → Sin beca ministerial, Apoyo entre pares activo |
| 4  | Derecho       | Riesgo alto      | Inactivo | Sí        | Inactivo           | **Estudiante 4 (Derecho)** – Riesgo alto → Sin beca ministerial, Apoyo entre pares activo |
| 5  | Derecho       | Riesgo medio     | Activo   | Sí        | Activo             | **Estudiante 5 (Derecho)** – Riesgo medio → Apoyo entre pares activo, Centro de estudiantes activo |
| 6  | Medicina      | Riesgo alto      | Activo   | Sí        | Inactivo           | **Estudiante 6 (Medicina)** – Riesgo alto → Apoyo entre pares activo |
| 7  | Psicología    | Riesgo medio     | Inactivo | No        | Activo             | **Estudiante 7 (Psicología)** – Riesgo medio → Sin beca ministerial, Centro de estudiantes activo |
| 8  | Psicología    | Riesgo medio     | Inactivo | No        | Inactivo           | **Estudiante 8 (Psicología)** – Riesgo medio → Sin beca ministerial |
| 9  | Psicología    | Riesgo medio     | Inactivo | No        | Activo             | **Estudiante 9 (Psicología)** – Riesgo medio → Sin beca ministerial, Centro de estudiantes activo |
| 10 | Derecho       | Riesgo medio     | Activo   | No        | Inactivo           | **Estudiante 10 (Derecho)** – Riesgo medio → (Sin alertas prioritarias) |

**Lógica**: Alertas solo para Riesgo medio/alto + Sin beca ministerial. Prioriza estudiantes con red activa (apoyo pares/centro) pero sin cobertura estatal.
|


## 🛠️ Arquitectura del piloto
```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]





