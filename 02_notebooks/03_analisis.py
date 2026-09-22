import pandas as pd

# Cargar CVS limpios
# parse_dates --> Convierte automáticamente los valores de la columna 'fecha' de texto simple a objetos de fecha y hora (datetime).
ipc = pd.read_csv('01_datos/procesados/ipc_limpio.csv', parse_dates=['fecha'])
sal = pd.read_csv('01_datos/procesados/salarios_limpio.csv', parse_dates=['fecha'])

# Unir por fecha (Similar a un JOIN en SQL)
# how = 'inner' mantiene solo las fechas que existen en AMBAS tablas.
df = pd.merge(ipc,sal, on='fecha', how='inner')

# Verificar el rango de fechas con ambas tablas:
# print(f'Rango de fechas: {df.fecha.min} -> {df.fecha.max}')
# print(f'Total de meses: {len(df)}')

# Salario real = (indice de salarios / IPC acumulado) * 100
# Si sube más que el IPC --> ganó poder adquisitivo.
# Si sube menos que el IPC --> perdió poder adquisitivo.

df['salario_real_total'] = df['salario_total'] / df['ipc_acumulado'] * 100
df['salario_real_priv_reg'] = df['privado_reg'] / df['ipc_acumulado'] * 100
df['salario_real_publico'] = df['publico'] / df['ipc_acumulado'] * 100

# Variación anual del IPC (comparar con el mismo mes del AÑO ANTERIOR)
# shift(12) desplaza la misma columna 12 posiciones hacia delante.

df['ipc_variacion_anual'] =  (
    (df['ipc_acumulado'] / df['ipc_acumulado'].shift(12) - 1) * 100
)

# Guardar análisis completo 
df.to_csv('01_datos/procesados/analisis_completo.csv', index=False)

# Inflación acumulada total del período
ipc_total = df['ipc_acumulado'].iloc[-1] - 100
print(f'Inflación acumulada: {ipc_total:.1f}%')

# Mes con mayor inflación mensual
mes_pico = df.loc[df['ipc_variacion_mensual'].idxmax(), 'fecha']
val_pico = df['ipc_variacion_mensual'].max()
print(f'Pico mensual: {mes_pico.strftime("%B %Y")} -> {val_pico:.1f}%')

# Variación del salario real total
sal_real_cambio = df['salario_real_total'].iloc[-1] - df['salario_real_total'].iloc[0]
print(f'Cambio en salario real: {sal_real_cambio:.1f} puntos')