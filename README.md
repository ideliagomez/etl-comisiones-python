Proceso ETL para Consolidación de Comisiones

Descripción:
Script Python que automatiza el proceso ETL (Extraer, Transformar, Cargar) para consolidar archivos de comisiones comerciales en un único dataset listo para análisis.

Características principales:
- Unifica múltiples reportes de Excel en una sola base de datos
- Valida y limpia los datos automáticamente
- Genera reportes consolidados listos para usar

Funcionalidades técnicas:

  Extracción (E):
    - Lee archivos Excel (.xlsx) desde carpetas específicas
    - Soporta estructuras de directorios variables
    - Detecta y reporta archivos corruptos o inaccesibles

  Transformación (T):
    - Combina datos de múltiples fuentes
    - Identifica y maneja:
        IDs de venta duplicados
        Valores nulos o faltantes
    - Estandariza formatos y estructuras

  Carga (L):
    - Exporta los datos consolidados a Excel
    - Incluye metadatos del proceso

Requisitos del sistema:
- Python 3.6 o superior
- Bibliotecas requeridas:
    pandas
    openpyxl

Instalación:
1. Instalar dependencias:
pip install pandas openpyxl

Estructura de carpetas recomendada:
documentos/
└─ comisiones/
   └─ [nombre_carpeta]  # Ejemplo: "1-enero-2025"
      ├─ archivo1
      ├─ archivo2
      ...


Modo de uso:
1. Ejecutar el script
2. Ingresar el nombre de la carpeta cuando se solicite
3. Revisar el archivo de salida "consolidado_final.xlsx"

Validaciones incluidas:
- Verificación de duplicados
- Detección de valores nulos
- Consistencia de estructura

Limitaciones conocidas:
- Tamaño máximo recomendado por archivo: 50MB
- Requiere estructura de columnas consistente
- No soporta hojas protegidas con contraseña

Archivo de salida:
- Nombre: consolidado_final.xlsx
- Formato: Excel estándar
- Incluye todos los datos procesados
