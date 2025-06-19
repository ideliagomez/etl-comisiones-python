""" Script para cargar archivos Excel de comisiones y consolidados desde carpetas específicas, 
unirlos en un único DataFrame, validar duplicados y nulos, y exportar el resultado a Excel. """

import os
import pandas as pd

def cargar_archivos():
    input_comisiones = input("Introduce la carpeta de comisiones (ej: '1-enero-2025'): ").strip()
    base_comisiones = r"C:\Users\admin\Documents\comisiones"
    ruta_comisiones = os.path.normpath(os.path.join(base_comisiones, input_comisiones))

    def cargar(ruta):
        if not os.path.exists(ruta):
            print("Error: La carpeta no existe.")
            return {}

        archivos = {}
        for f in os.listdir(ruta):
            if f.endswith('.xlsx'):
                try:
                    archivo_path = os.path.join(ruta, f)
                    df = pd.read_excel(archivo_path)
                    archivos[f] = df
                except Exception as e:
                    print(f"Error al cargar {f}: {str(e)}")
        return archivos

    comisiones = cargar(ruta_comisiones)

    return comisiones

def validar_datos(df_unido):
    duplicados = df_unido.duplicated(subset=['id_venta'], keep=False)
    if duplicados.any():
        print("\n¡Advertencia! Se encontraron IDs de venta duplicados:")

    nulos = df_unido.isnull().sum()
    if nulos.any():
        print("\n¡Advertencia! Se encontraron valores nulos:")
        
    return df_unido

if __name__ == "__main__":
    comisiones = cargar_archivos()
    if comisiones:
        dfs_comisiones = list(comisiones.values())
        df_unido = pd.concat(dfs_comisiones, ignore_index=True)
        df_unido = validar_datos(df_unido)
        df_unido.to_excel("consolidado_final.xlsx", index=False)
    
    print("\nResumen final:")
    print(f"- Archivos de comisiones cargados: {len(comisiones)}")
 