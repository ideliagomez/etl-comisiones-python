# Proceso ETL para Consolidación de Comisiones

![ETL Workflow](https://github.com/ideliagomez/etl-comisiones-python/blob/master/img/front_page.png?raw=true)

> Script en Python que automatiza el proceso **ETL (Extraer, Transformar, Cargar)** para consolidar archivos de comisiones comerciales en un único dataset listo para análisis.

---

##  Características principales

-  Unifica múltiples reportes de Excel en una sola base de datos
-  Valida y limpia los datos automáticamente
-  Genera reportes consolidados listos para usar

---

## ⚙️ Funcionalidades técnicas

###  Extracción (E)
- Lee archivos Excel (`.xlsx`) desde carpetas específicas
- Soporta estructuras de directorios variables
- Detecta y reporta archivos corruptos o inaccesibles

###  Transformación (T)
- Combina datos de múltiples fuentes
- Identifica y maneja:
  - IDs de venta duplicados
  - Valores nulos o faltantes
- Estandariza formatos y estructuras

###  Carga (L)
- Exporta los datos consolidados a Excel
- Incluye metadatos del proceso

---

##  Requisitos del sistema

- Python 3.6 o superior  
- Bibliotecas necesarias:

```bash
pip install pandas openpyxl

> **Nota sobre los datos**: Los datos utilizados en este proyecto son simulados y no pertenecen ni representan información real de ninguna empresa u organización.

