"El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste." — Principio materno, SUR DAO

SUR DAO – Piloto Retención Estudiantil USACH/Mineduc
Reciprocidad > Burocracia. Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

📊 Problema: 71k anual → 500k+
Reciprocidad > Burocracia
Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

📊 Problema: 71k anual → 500k+ sombra acumulada
Año	Ingresos	Deserción (28.8%)	Stock acumulado
2020	250k	72k	504k
2021	250k	72k	432k
2022	250k	72k	360k
Total 7 años	—	—	~500k estudiantes sombra
Fuente: Mineduc/SIES (28.8% primer año) + USACH Anuario (14.6% reprobación).

⚙️ Funcionalidad
```st.subheader("Alertas combinadas")
for i, row in df_full.iterrows():
    riesgo = row["CategoriaRiesgo"]
    if riesgo in ["Riesgo alto", "Riesgo medio"]:
        acciones = []
        if row["EstadoBeca"] == "Inactivo":
            acciones.append("Sin beca ministerial")
        if row["ApoyoPar"] == "Sí":
            acciones.append("Apoyo entre pares activo")
        if row["CentroEstudiantes"] == "Activo":
            acciones.append("Centro de estudiantes activo")
        
        st.markdown(f"**Estudiante {row['ID']} ({row['Carrera']})** – {riesgo} → " + ", ".join(acciones))

```
 A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]

```

🎯 Propósito / Purpose
Detectar tempranamente estudiantes en riesgo (congelamiento, deserción) → activar apoyos VRAE/VRA.
Python dashboard con datos SCT anonimizados + capas institucionales y comunitarias.
📄 Documentación completa: [Parece que el resultado no era seguro para mostrar. ¡Cambiemos de enfoque y probemos algo diferente!]

```
📊 Datos clave
28.8% tasa de deserción en primer año (SIES).

427 renuncias en USACH durante 2022.

14.6% deserción permanente (OECD).

Falta de coordinación entre MINEDUC, JUNAEB, becas internas y apoyo comunitario.

```
🔔 Alertas combinadas (ejemplos del piloto)
ID	Carrera	Riesgo	Beca	Apoyo Par	Centro Estudiantes	Alerta generada
1	Arquitectura	Medio	Inactivo	No	Inactivo	Sin beca ministerial
2	Derecho	Medio	Inactivo	Sí	Activo	Sin beca + Apoyo pares + Centro activo
4	Derecho	Alto	Inactivo	Sí	Inactivo	Riesgo alto + Sin beca + Apoyo pares
Lógica: Alertas solo para Riesgo medio/alto + Sin beca ministerial. Se prioriza acompañamiento donde hay red activa (pares/centro) pero falta cobertura estatal.

```
🛠️ Arquitectura del piloto
```flowchart TD
    Riesgo["📊 Riesgo académico"]
    Becas["🎓 Becas ministeriales/internas"]
    Junaeb["🍽️ JUNAEB"]
    Pares["🤝 Apoyo entre pares"]
    Centro["🏛️ Centro de estudiantes"]

    Riesgo --> Becas
    Riesgo --> Junaeb
    Riesgo --> Pares
    Riesgo --> Centro
```

flowchart TD
``` Riesgo["📊 Riesgo académico"]
    Becas["🎓 Becas ministeriales/internas"]
    Junaeb["🍽️ JUNAEB"]
    Pares["🤝 Apoyo entre pares"]
    Centro["🏛️ Centro de estudiantes"]

    Riesgo --> Becas
    Riesgo --> Junaeb
    Riesgo --> Pares
    Riesgo --> Centro



```



🛠️ Arquitectura del piloto
```flowchart TD A[Datos SCT anon.] --> B[Motor de reglas en Python] B --> C[Dashboard VRA/VRAE] C --> D[Alertas psicosociales] D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas] E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]

⚙️ Funcionalidad (ejemplo en Python) st.subheader("Alertas combinadas") for i, row in df_full.iterrows(): riesgo = row["CategoriaRiesgo"] if riesgo in ["Riesgo alto", "Riesgo medio"]: acciones = [] if row["EstadoBeca"] == "Inactivo": acciones.append("Sin beca ministerial") if row["ApoyoPar"] == "Sí": acciones.append("Apoyo entre pares activo") if row["CentroEstudiantes"] == "Activo": acciones.append("Centro de estudiantes activo")

    st.markdown(f"**Estudiante {row['ID']} ({row['Carrera']})** – {riesgo} → " + ", ".join(acciones))
0 commit comments
Comments
0
```


