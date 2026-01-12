Earth-Commons-DAO / SUR DAO
Gobernanza descentralizada para los bienes comunes y trayectorias educativas flexibles.  
👉 SUR DAO Live

🌍 Visión y Propósito / Vision & Purpose
ES: Crear un sistema DAO que articule territorios, comunidades y universidades para proteger y reconvertir capital humano y ecológico.
EN: Build a DAO system that connects territories, communities, and universities to protect and reconvert human and ecological capital.

🎯 Propósito
Retención estudiantil y reconversión de créditos académicos.
Gobernanza comunitaria de datos y recursos.
Activación de apoyos institucionales y humanos.

📊 Crisis: 500k Estudiantes Sombra
28.8% deserción en primer año (SIES).
500k créditos vigentes acumulados en estudiantes que abandonaron.
Capital humano latente estimado: $6B.

🔄 Match Deserción → Afines Prioritarios
| Carrera Origen       | Tasa Deserción | Destino Afín Prioritario    | % Créditos SCT |
| -------------------- | -------------- | --------------------------- | -------------- |
| Ing. Computación     | 40.5%          | Automatización Industrial A | 75%            |
| Ciencias Exactas     | 59.5%          | Ing. Civil + Pedagogía A/B  | 60%            |
| Técnico Construcción | 40%            | Ing. Civil Construcción A   | 80%            |
| Logística            | 35%            | Gestión Pública A           | 65%            |
Datos basados en convalidaciones SCT reales; >60% habilita "win-win" institucional por Ley 21.091


🧩 Actores y Beneficios
| Actor         | Problema Actual          | SUR DAO Solución                 | Ganancia $ Anual |
| ------------- | ------------------------ | -------------------------------- | ---------------- |
| MINEDUC       | 76% retención meta FES   | +20% reingresos                  | +$500B           |
| Universidades | -15% matrícula gratuidad | 80% créditos → nueva matrícula   | +$1.2B           |
| Estudiante    | Deuda + 0 créditos       | Trueque 1.5 años → título        | Sin deuda        |
| SENCE         | Déficit técnicos         | Match deserción → Automatización | 85% empleo       |

Ley 21.091 Art.28: SCT convalidación OBLIGATORIA.
Filosofía: Los créditos no se pierden → se reconvierten inteligentemente.

  
  def winwin_ues(match):
    """
    Evalúa si un caso de reconversión de créditos SCT cumple condiciones
    para ser considerado 'win-win' entre UES y MINEDUC.
    
    Parámetros:
        match (dict): {
            "ley_21091": bool,
            "pct_sct": int,
            "riesgo_psicosocial": bool,
            "demanda_laboral": bool
        }
    """
    if not match.get("ley_21091", False):
        return "❌ No cumple Ley 21.091 (convalidación obligatoria)"

    if match.get("pct_sct", 0) < 60:
        return "⚠️ Créditos insuficientes para reconversión (>60% requerido)"

    if match.get("riesgo_psicosocial", False):
        return "🧠 Derivar a apoyo psicosocial antes de reconversión"

    if match.get("demanda_laboral", False):
        return "💰 UES: Nueva matrícula + MINEDUC: Retención + SENCE: Empleabilidad"

    return "📌 Revisar caso: cumple requisitos mínimos pero falta validación de demanda"



📊 Mapa de Oportunidades
🔴 Zona Crítica: Psicología / Periodismo (deserción + saturación).

🟢 Zona Oportunidad: Computación / Construcción (deserción alta → demanda).

🏗️ Arquitectura SUR DAO
mermaid
flowchart TD
  A[Datos SCT anon.] --> B[Motor de reglas]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]


Flujo de datos: SCT anónimos → motor de reglas → dashboards institucionales → alertas psicosociales → capas de apoyo.
Infraestructura: nodos y data centers comunitarios.
Capas de gobernanza: institucional, territorial, humana.

🛣️ Roadmap
Fase 1: Piloto SUR DAO (USACH/Mineduc).
Fase 2: Expansión a otras universidades y territorios.
Fase 3: Integración con Earth-Commons-DAO para bienes comunes ecológicos.

🤝 Cómo Participar
Instituciones: colaborar en reconversión de créditos y dashboards.
Estudiantes: acceder a alertas y apoyos.
Comunidad: aportar nodos, data centers y acompañamiento humano.
Contribuidores técnicos: revisar piloto_sur.py, docs/, manifiestos/.

📜 Licencia y Valores
Código abierto.
Principios: transparencia, reciprocidad, sostenibilidad.

![SUR DAO Live](https://img.shields.io/badge/SUR%20DAO-Live-brightgreen?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-Yes-blue?style=flat-square)
![Community Driven](https://img.shields.io/badge/Community-Driven-orange?style=flat-square)
![DAO Governance](https://img.shields.io/badge/DAO-Governance-purple?style=flat-square)
![Made in Chile](https://img.shields.io/badge/Made%20in-Chile-red?style=flat-square)

  
