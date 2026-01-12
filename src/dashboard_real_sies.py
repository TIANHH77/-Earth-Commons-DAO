import streamlit as st
from surdao_hibrido_v2 import surdao_hibrido

st.title("🚀 SUR DAO Live – Datos Reales SIES 2025")

res = surdao_hibrido()

col1, col2, col3 = st.columns(3)
col1.metric("Carreras Nacionales", res['general_carreras'])
col2.metric("USACH 3+ Años", res['usach_prior_3mas'])
col3.metric("Capital $MM", f"${res['capital_recuperable_mm']:,.0f}")

st.subheader("Top 50 USACH Prioritarios")
st.dataframe(res['top_50'].head(20))

