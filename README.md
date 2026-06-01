# Automatización de Limpieza de Datos con Python y Pandas

Este proyecto consiste en un script de Python desarrollado para **automatizar la depuración y normalización de bases de datos** (como archivos de Excel o CSV). 

El objetivo principal es resolver los errores de carga humana más comunes (espacios fantasma, inconsistencia en tildes, formatos de texto y duplicados) asegurando la integridad de los datos para su posterior análisis o migración a sistemas corporativos.

## 🛠️ Tecnologías Utilizadas
* **Python 3**
* **Pandas**: Para la manipulación y procesamiento estructurado de los datos.
* **Openpyxl**: Para la lectura y escritura de archivos .xlsx de Excel.

## 📈 Problemas de Datos Resueltos en este Script

El script procesa de forma automática los siguientes dolores de cabeza habituales en bases de datos de más de 50,000 registros:

1. **Estandarización de Texto:** Remoción de espacios en blanco al principio y final de los campos (`.str.strip()`) y conversión uniforme a minúsculas (`.str.lower()`).
2. **Normalización Masiva de Tildes:** Implementación de un bucle optimizado que mapea y reemplaza vocales con acento por caracteres limpios, evitando duplicaciones por errores ortográficos (ej: unifica `lanús` y `lanus`).
3. **Validación y Limpieza de Teléfonos:** * Conversión forzada del tipo de dato a texto para evitar errores de lectura.
   * Remoción masiva de guiones y espacios en el medio de los números.
   * Remoción de prefijos redundantes (ej: unificación de prefijos `011` a `11`).
4. **Tratamiento de Registros Vacíos:** Reemplazo inteligente de valores nulos (`NaN`) por etiquetas corporativas prolijas como `"Sin Registrar"`.
5. **Eliminación de Duplicados:** Depuración de la tabla entera (`.drop_duplicates()`) una vez que los datos críticos ya fueron homogeneizados.

## 📂 Estructura del Proyecto
```text
├── datos_sucios.xlsx    # Archivo Excel original con errores de carga.
├── limpiar_datos.py     # Script principal de automatización en Python.
└── datos_limpios.xlsx   # Producto final depurado listo para usar.
