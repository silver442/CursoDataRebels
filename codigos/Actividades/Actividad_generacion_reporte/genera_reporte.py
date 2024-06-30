import pandas as pd
from datetime import datetime
import os

# Obtener la ruta del directorio donde está el script
directorio_script = os.path.dirname(os.path.abspath(__file__))

# Ruta al archivo de datos (CSV)
ruta_datos = os.path.join(directorio_script, 'venta.csv')

# Ruta al archivo de registro
ruta_log = os.path.join(directorio_script, 'log.txt')

def escribir_log(mensaje):
    with open(ruta_log, 'a') as log:
        log.write(f'{datetime.now()}: {mensaje}\n')

try:
    # Leer los datos
    datos = pd.read_csv(ruta_datos)
    escribir_log('Datos leídos correctamente')

    # Procesar los datos (ejemplo simple: sumar una columna llamada 'ventas')
    reporte = datos['ventas'].sum()
    escribir_log(f'Procesamiento de datos completado: Total de ventas = {reporte}')

    # Guardar el reporte con un timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    ruta_reporte = os.path.join(directorio_script, f'reporte_{timestamp}.txt')
    with open(ruta_reporte, 'w') as file:
        file.write(f'Reporte generado el {timestamp}\n')
        file.write(f'Total de ventas: {reporte}\n')
    escribir_log(f'Reporte generado y guardado en {ruta_reporte}')

except Exception as e:
    escribir_log(f'Error: {str(e)}')

print(f'Reporte generado y guardado en {ruta_reporte}')
