import streamlit as st
import pandas as pd
import plotly.express as px
import unicodedata

# -----------------------------
# Función para normalizar columnas
# -----------------------------
def normalize_columns(df):
    """
    Normaliza los nombres de columnas:
    - Elimina espacios al inicio y al final
    - Convierte todo a minúsculas
    - Reemplaza tildes y caracteres especiales por su forma básica
    """
    def clean(col):
        col = col.strip().lower()
        col = unicodedata.normalize('NFKD', col).encode('ascii', errors='ignore').decode('utf-8')
        return col
    df.columns = [clean(c) for c in df.columns]
    return df

# -----------------------------
# Configuración de la app
# -----------------------------
st.set_page_config(page_title="SUR DAO USACH", layout="wide", page_icon="🌑")
st.title("🌑 SUR DAO - Custodia de Trayectorias USACH")
st.markdown("**Datos reales SIES 2025 + USACH** | Infraestructura porosa para retención")

# -----------------------------
# Función para cargar CSV con fallback demo
# -----------------------------
@st.cache_data
def load_csv(path, demo_df=None, index_col=None):
    try:
        df = pd.read_csv(path)
        if index_col and index_col in df.columns:
            df.set_index(index_col, inplace=True)
        return df
    except FileNotFoundError:
        if demo_df is not None:
            st.warning(f"{path} no encontrado - usando demo")
            return demo_df
        else:
            st.warning(f"{path} no encontrado - vacío")
            return pd.DataFrame()

# -----------------------------
# Cargar datasets
# -----------------------------
real = load_csv("data/surdao_real_matches_2025.csv", demo_df=pd.DataFrame({
    "carrera": ["Ing.Civil Informática", "Psicología"],
    "desercion_pct": [40.5, 45.2],
    "creditos_sct": [208, 192],
    "impacto_mm": [2.5, 2.3]
}))

hibrido = load_csv("data/surdao_hibrido_v2.csv", demo_df=pd.DataFrame({
    "Carrera": ["Ing.Civil Informática", "Psicología"],
    "Años_Est": [7, 5],
    "Creditos": [280, 200],
    "Valor_Humano_MM": [3.36, 2.40],
    "Vacantes_Destino": [600, 150],
    "Match_Afin": ["Automatización 🟢", "🔴 Crítica Apoyo"]
}))

becas   = load_csv("data/becas.csv", index_col="ID")
junaeb  = load_csv("data/junaeb.csv", index_col="ID")
mineduc = load_csv("data/mineduc.csv", index_col="ID")
usach   = load_csv("data/usach.csv")
pares   = load_csv("data/pares.csv", index_col="ID")

# 🔮 Normalizar todos en bloque
datasets = [real, hibrido, becas, junaeb, mineduc, usach, pares]
datasets = [normalize_columns(df) for df in datasets]
real, hibrido, becas, junaeb, mineduc, usach, pares = datasets

# -----------------------------
# Merge maestro
# -----------------------------
df_master = real.merge(hibrido, on="carrera", how="outer")
df_master = df_master.merge(usach, on="carrera", how="outer")
df_master = df_master.merge(becas, left_index=True, right_index=True, how="outer")
df_master = df_master.merge(junaeb, left_index=True, right_index=True, how="outer")
df_master = df_master.merge(mineduc, left_index=True, right_index=True, how="outer")
df_master = df_master.merge(pares, left_index=True, right_index=True, how="outer")

# 👀 Mostrar columnas resultantes para verificar
st.write("### Columnas en df_master:", df_master.columns.tolist())

# Exportar automáticamente a CSV maestro
df_master.to_csv("data/surdao_master.csv", index=False)

# -----------------------------
# KPIs
# -----------------------------
col1, col2, col3 = st.columns(3)
col1
