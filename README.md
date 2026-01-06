# Piloto SUR DAO para USACH: Herramienta de Monitoreo y Apoyo a Estudiantes

## 1. Propósito del piloto

Desarrollar y probar una **herramienta de monitoreo temprano de riesgo de desvinculación** para estudiantes de pregrado, que permita activar apoyos oportunos usando datos ya disponibles en la institución, sin cambiar reglamentos ni estructuras internas.

La propuesta se alinea con:
- Modelo Educativo Institucional USACH.
- Normativa de Formación Integral (Res. Exenta 008417.05.12.19).[file:13]
- Reglamentos de régimen de estudios de pregrado.

## 2. Problema que aborda

Actualmente, la institución dispone de datos académicos y normativas de formación integral, pero no cuenta con un sistema integrado que:

- Detecte tempranamente estudiantes en riesgo de desvinculación (congelamiento, abandono, renuncia).
- Conecte automáticamente esos casos con ofertas de apoyo (formación integral, bienestar, beneficios).[file:13]
- Genere alertas accionables para unidades responsables (VRA, VRAE, unidades académicas).

El resultado es una **“capa sombra” de estudiantes** que se pierden del sistema sin seguimiento suficiente, pese a existir marcos normativos que reconocen su derecho a espacios formativos y de bienestar.[file:13]

## 3. Fundamento normativo mínimo

El piloto se basa exclusivamente en normativa y prácticas ya vigentes en USACH:

- **Formación Integral – Art. 1 a 4**: define actividades orientadas al bienestar y desarrollo integral, reconociéndolas dentro de la trayectoria curricular.[file:13]
- **Dimensiones clave – Art. 3 (e y f)**:
  - Competencias digitales y tecnológicas.
  - Desarrollo de idiomas y lenguas.[file:13]
- **Créditos Académicos Transferibles – Art. 8 y 9**:
  - Actividades de formación integral y cursos optativos asignan SCT, lo que permite su trazabilidad y movilidad.[file:13]

El piloto no modifica esta normativa, solo la operacionaliza con datos y alertas.

## 4. Descripción de la herramienta

La herramienta consiste en un **dashboard y motor de reglas** que:

- Consume datos anónimos a nivel de cohorte (matrícula, congelamientos, renuncias, reprobaciones, avance en SCT).
- Aplica reglas simples de riesgo (ej.: N créditos reprobados, X semestres congelados, sin inscripción en actividades de formación integral).[file:13]
- Genera paneles para:
  - Vicerrectoría Académica (visión global por cohorte y carrera).
  - Vicerrectoría de Apoyo al Estudiante (foco en bienestar).
  - Unidades académicas (alertas por carrera).

Opcionalmente, puede integrarse un sistema de notificaciones (correo o mensajería) hacia equipos humanos responsables, nunca directo al estudiante sin pasar por dichas unidades.

## 5. Alcance del piloto USACH

**Escala mínima de prueba (recomendado):**

- 1 cohorte de primer año en 1–2 carreras de alta matrícula.
- Periodo de observación: 1 año académico.
- Variables usadas:
  - Matrícula, inscripción de asignaturas, congelamientos, renuncias.
  - Registro de participación en actividades de formación integral (cursos, talleres, programas).[file:13]

**Resultados esperados:**

- Línea base cuantitativa de:
  - Tasa de desvinculación por cohorte.
  - Porcentaje de estudiantes en riesgo que acceden efectivamente a oferta de formación integral.
- Propuestas de ajuste a la oferta de formación integral y a los flujos de derivación a VRAE, basadas en datos.

## 6. Privacidad y anonimato

- El piloto se diseña para operar inicialmente con **datos agregados y/o anonimizados** (sin identificación nominativa de estudiantes).
- Cualquier futura fase con datos nominales:
  - Requiere aprobación ética y jurídica institucional.
  - Se limita estrictamente a equipos humanos autorizados (p. ej., unidades de apoyo psicosocial).

El código fuente y la documentación se ofrecen con foco en **replicabilidad institucional**, no en casos personales.

## 7. Implementación técnica resumida

- Lenguaje: Python.
- Componentes:
  - Módulo de ingestión de datos (CSV/BD institucional).
  - Motor de reglas de riesgo.
  - Dashboard web simple para visualización.
- Despliegue:
  - Servidor interno o entorno controlado de la universidad.
  - Sin exposición de datos a servicios externos en fases iniciales.

## 8. Invitación a colaboración

Se propone conformar un **equipo mixto** (académicos, profesionales de apoyo estudiantil y estudiantes) para:

- Definir reglas de riesgo contextualizadas.
- Revisar periódicamente los resultados del piloto.
- Formular recomendaciones de política interna basadas en la evidencia generada.

El objetivo de SUR DAO en este contexto es servir como **herramienta modular** que la USACH pueda adoptar, adaptar o descartar libremente, sin compromisos tecnológicos ni de gobernanza ajenos a su propia estructura institucional.
