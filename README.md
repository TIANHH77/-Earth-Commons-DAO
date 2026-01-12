# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc  

> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
> — Principio materno  

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

| Carrera origen        | Tasa deserción | Destino afín prioritario | % Créditos SCT reconocidos |
|-----------------------|----------------|--------------------------|----------------------------|
| Ing. Computación      | 40.5%          | Automatización Industrial A | 80% |
| Ciencias Exactas      | 59.5%          | Ing. Civil + Pedagogía A/B | 65% |
| Técnico Construcción  | 40%            | Ing. Civil Construcción A | 75% |
| Logística             | 35%            | Gestión Pública A         | 70% |

**Filosofía:** Los créditos **no se pierden** → se **reconvierten inteligentemente**.  

---

## 📊 Mapa de Oportunidades
- **Zona crítica**: carreras con alta deserción + alta saturación laboral (Psicología, Periodismo, Trabajo Social).  
- **Zona de oportunidad**: carreras con alta deserción pero baja saturación → reconversión hacia áreas deficitarias (ej. Computación → Automatización).  

---

## 🏗️ Arquitectura SUR DAO
```mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]





