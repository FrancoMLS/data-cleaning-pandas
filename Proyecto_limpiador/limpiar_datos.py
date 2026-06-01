import pandas as pd
import os

# Se carga el archivo sucio
ruta_archivo = os.path.join(os.path.dirname(__file__), "datos_sucios.xlsx")
df = pd.read_excel(ruta_archivo)

print("--- DATOS ORIGINALES ---")
print(df)

# Se ponen las primeras letras de cada palabra de la columna 'Nombre' en mayúscula
df['Nombre'] = df['Nombre'].str.title()

# Limpiamos la columna 'Localidad'
df['Localidad'] = df['Localidad'].str.strip()

tildes = {"á": "a", "é": "e", "í":"i", "ó":"o", "ú":"u"}
for con_tilde, sin_tilde in tildes.items():
    df['Localidad'] = df['Localidad'].str.replace(con_tilde, sin_tilde).str.title()

# Limpiamos la columna 'Teléfono'
df['Teléfono'] = df['Teléfono'].astype(str).str.replace("-", "").str.replace(" ", "").str.replace("nan", "Sin Registrar").str.removeprefix("0")

# Eliminamos los duplicados
df = df.drop_duplicates()

# Se guarda el resultado final
ruta_salida = os.path.join(os.path.dirname(__file__), "datos_limpios.xlsx")
df.to_excel(ruta_salida, index=False)
print("\n¡Base de datos depurada con éxito!")
print(df)