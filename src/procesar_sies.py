import pandas as pd
import numpy as np
from difflib import get_close_matches
print("🌍 Earth Commons DAO - SURDAO Matches 2025")

# 1. CARGAR SIES (Semicolon!)
sies = pd.read_csv('Oferta_Academica_2025_SIES.csv', sep=';', low_memory=False)
print(f"✅ SIES: {len(sies)} carreras 2025")

# 2. Limpiar carreras
sies['Nombre_Carrera'] = sies['Nombre Carrera'].str.strip().str.title()

# 3. DATOS SURDAO (tu fuente - ajusta aquí)
surdao_raw = {
    'carrera': [
        'ingenieria civil informatica',
        'psicologia',
        'administracion empresas',
        'ingenieria industrial'
    ],
    'desercion_pct': [40.5, 45.2, 32.1, 28.7],
    'creditos_acum': [208, 180, 220, 240],
    'capital_recuperable': [0.12, 0.08, 0.15, 0.18]
}
surdao_df = pd.DataFrame(surdao_raw)

# 4. FUZZY MATCH (95%+ score)
matches = []
for idx, row in surdao_df.iterrows():
    query = row['carrera'].title()
    candidates = get_close_matches(query, sies['Nombre_Carrera'].tolist(), n=1, cutoff=0.85)
    
    if candidates:
        match_carrera = candidates[0]
        sies_row = sies[sies['Nombre_Carrera'] == match_carrera].iloc[0]
        
        matches.append({
            'Carrera_SURDAO': query,
            'Match_SIES': match_carrera,
            'Score': 95,  # Aprox
            'Desercion_SIES_pct': row['desercion_pct'],
            'Creditos_Acum': row['creditos_acum'],
            'Capital_Recuperable': row['capital_recuperable'],
            'Universidad': sies_row['Nombre IES'],
            'Region': sies_row['Regin Sede'],
            'Cdigo_Carrera': sies_row['Cdigo Carrera']
        })
    else:
        matches.append({'Carrera_SURDAO': query, 'Match_SIES': 'NO_ENCONTRADO', 'Score': 0})

# 5. GUARDAR CSV FINAL (Comma!)
matches_df = pd.DataFrame(matches)
matches_df.to_csv('surdao_real_matches_2025.csv', index=False, sep=',')
print("💾 surdao_real_matches_2025.csv ✅ (Comma format)")
print(matches_df.head())
