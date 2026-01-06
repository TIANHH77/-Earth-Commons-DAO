# 🌐 Earth Commons DAO – Índice Maestro
# SUR DAO - Piloto Resiliencia Educativa 🇨🇱➡️🇦🇷

**Reciprocidad > Burocracia**. Herramienta descentralizada que detecta "capa sombra" (71k estudiantes congelados/año, 28.8% primer año deserción) y alerta redes humanas (WhatsApp 9AM ARG).[file:13]

## 🚨 Problema Estructural
- **Mineduc/SIES**: 28.8% deserción año 1 (49k), 14.6% permanente (22k). [datos.gob.cl]
- **USACH**: Renuncias 2022: 427 (4.5%). Normativa Formación Integral (Res. Exenta 008417.05.12.19) obliga apoyo psicosocial/diversidad/ciudadanía – NO cumple para congelados.[file:13]
- **Tu Caso**: 6 silos fallan (USACH/JUNAEB/VRAE/etc), deuda 2.5M sin apoyo.

## 🌐 Arquitectura DAO
- **Nodos x6**: USACH, JUNAEB, VRAE, etc. Pandas scrape + triggers riesgo.
- **Dashboard**: Streamlit live (sur_dashboard.py).
- **Alertas**: GitHub Actions cron 9AM → Twilio WhatsApp "Fase 1: Renuncias >400".
- **Datos**: CSV Mineduc (1.4M registros), USACH renuncias histórico.

| Año | Renuncias USACH | Tasa |
|-----|-----------------|------|
| 2022| 427             | 4.5% |
| 2021| 567             | 6.0% |
| 2020| 450             | 5.2% |[conversation_history:15]

## 📋 Deploy 1-Click
1. `pip install streamlit pandas twilio`
2. Secrets GitHub: `TWILIO_SID`, `ASISTENTE_PHONE` (Haroldo).
3. `streamlit run sur_dashboard.py` → share.streamlit.io.
4. Actions YAML auto-cron.

## 🇦🇷 Convalidación ARG
Créditos SCT Formación Integral USACH transferibles (DFL 149/1981, Res.7441/2017). UTN FRSN TUPAD: "Excepción post-deadline + normativa integral".[file:13][conversation_history:8]

## 🤝 Contribuir
- Fork → PR con nodos nuevos.
- Migrate Argentina 2026: Junín base + paramotor.

**Santiago Horta Hurtado** – Herramienta + espíritu liberados. No más USACH.


