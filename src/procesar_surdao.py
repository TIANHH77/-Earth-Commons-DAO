import pandas as pd

# 1. Cargar SIES base
sies = pd.read_csv("data/surdao_real_matches_2025.csv")

# 2. Descargar MiFuturo (empleabilidad)
mifuturo = pd.read_csv("data/mifuturo_empleabilidad_2025.csv", sep=";")

# 3. Mapear empleabilidad a SIES
sies["Empleabilidad_%"] = sies["Codigo_Carrera"].map(
    mifuturo.set_index("Codigo_Carrera")["Empleabilidad_%"]
)

# 4. Match final con tabla SURDAO
matches_df = sies.copy()
matches_df["Empleabilidad"] = matches_df["Carrera_SURDAO"].map(
    sies.set_index("Carrera_SURDAO")["Empleabilidad_%"]
)

# 5. Guardar SUPER CSV
matches_df.to_csv("data/surdao_super_matches_2026.csv", index=False)

