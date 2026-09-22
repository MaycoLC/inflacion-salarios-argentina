import pandas as pd
from pathlib import Path

df_original = pd.read_excel(
    '01_datos/original/ipc_nacional.xls',
    sheet_name='Variación mensual IPC Nacional',
    header=5
)

# El archivo original tiene una fila por categoria y una columna por mes.
# Convertimos la fila "Nivel general" a un formato largo.
categoria_columna = df_original.columns[0]
filas_nivel_general = df_original.loc[
    df_original[categoria_columna].astype('string').str.strip().str.casefold().eq(
        'nivel general'
    )
]
if filas_nivel_general.empty:
    raise ValueError('No se encontró la fila Nivel general en el Excel.')

df = filas_nivel_general.iloc[[0]].drop(columns=categoria_columna).T.reset_index()
df.columns = ['fecha', 'ipc_variacion_mensual']

df['fecha'] = pd.to_datetime(df['fecha'])
df['ipc_variacion_mensual'] = pd.to_numeric(
    df['ipc_variacion_mensual'], errors='coerce'
)
df = df.dropna().sort_values('fecha').reset_index(drop=True)

# Calcular el índice acumulado con base 100 en diciembre de 2016.
df['ipc_acumulado'] = (
    (1 + df['ipc_variacion_mensual'] / 100).cumprod() * 100
).round(6)

# Guardar como CSV limpio
salida = Path('01_datos/procesados/ipc_limpio.csv')
salida.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(salida, index=False, encoding='utf-8')
print('IPC limpio guardado. Filas: ', len(df))

# Verificación 
df_limpio = pd.read_csv("01_datos/procesados/ipc_limpio.csv")

print(df_limpio.head())
print(df_limpio.shape)
print(df_limpio.columns)