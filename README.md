
> "El respeto no se gana. Cuando vayas a algún lugar, trata de que después de irte, hayas aportado en algo ahí, que ojalá esté mejor de como cuando llegaste."  
— Principio materno, SUR DAO

# SUR DAO – Piloto Retención Estudiantil USACH/Mineduc

**Reciprocidad > Burocracia**  
Herramienta open-source que detecta estudiantes "sombra" (congelados, sin beca, riesgo alto) y alerta redes institucionales para acompañamiento proactivo.

---

## 📊 Problema: 71k anual → 500k+ sombra acumulada

| Año  | Ingresos | Deserción (28.8%) | Stock acumulado |
|------|----------|-------------------|-----------------|
| 2020 | 250k     | 72k               | 504k            |
| 2021 | 250k     | 72k               | 432k            |
| 2022 | 250k     | 72k               | 360k            |
| **Total 7 años** | — | — | ~500k estudiantes sombra |

**Fuente:** Mineduc/SIES (28.8% primer año) + USACH Anuario (14.6% reprobación).

---

## ⚙️ Funcionalidad

```python
st.subheader("Alertas combinadas")
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





  A[Datos SCT anon.] --> B[Motor de reglas en Python]
  B --> C[Dashboard VRA/VRAE]
  C --> D[Alertas psicosociales]
  D --> E[Capas institucionales: MINEDUC, JUNAEB, Becas]
  E --> F[Capas humanas: Apoyo entre pares, Centro de estudiantes]





