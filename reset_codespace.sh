#!/bin/bash

echo "🌑 SUR DAO Ritual: matar todo y sincronizar con git..."

# 1. Cerrar procesos de Streamlit (si quedaran vivos)
pkill -f streamlit

# 2. Limpiar dependencias y reinstalar
echo "🔄 Reinstalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall

# 3. Sincronizar con git
echo "🐙 Sincronizando con git..."
git fetch --all
git reset --hard origin/main

# 4. Reiniciar la app
echo "🚀 Lanzando SUR DAO..."
python -m streamlit run src/piloto_sur.py
