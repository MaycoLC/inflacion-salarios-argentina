import pandas as pd
from pathlib import Path

df_original = pd.read_excel(
    '01_datos/original/indice_salarios.xls',
    sheet_name='Cuadro 1',
    header=4
)

# El cuadro tiene encabezados combinados: año y mes están en las dos primeras
# columnas, y cada sector tiene una columna de variación y otra de índice.
df_sal = df_original.iloc[:, [0, 1, 3, 5, 7, 9, 11]].copy()
df_sal.columns = [
    'anio',
    'mes',
    'privado_reg',
    'publico',
    'total_registrado',
    'privado_no_reg',
    'salario_total',
]

df_sal['anio'] = pd.to_numeric(df_sal['anio'], errors='coerce').ffill()
meses = {
    'Enero': 1,
    'Febrero': 2,
    'Marzo': 3,
    'Abril': 4,
    'Mayo': 5,
    'Junio': 6,
    'Julio': 7,
    'Agosto': 8,
    'Septiembre': 9,
    'Octubre': 10,
    'Noviembre': 11,
    'Diciembre': 12,
}
df_sal['mes'] = df_sal['mes'].astype('string').str.strip().map(meses)
df_sal['fecha'] = pd.to_datetime(
    {'year': df_sal['anio'], 'month': df_sal['mes'], 'day': 1},
    errors='coerce'
)

columnas_indice = [
    'fecha',
    'salario_total',
    'privado_reg',
    'privado_no_reg',
    'publico',
    'total_registrado',
]
df_sal = df_sal[columnas_indice]
for columna in columnas_indice[1:]:
    df_sal[columna] = pd.to_numeric(df_sal[columna], errors='coerce')
df_sal = df_sal.dropna().sort_values('fecha').reset_index(drop=True)

# Guardar como CSV limpio
salida = Path('01_datos/procesados/salarios_limpio.csv')
salida.parent.mkdir(parents=True, exist_ok=True)
df_sal.to_csv(salida, index=False, encoding='utf-8')
print('Salarios limpio guardado. Filas: ', len(df_sal))

# Verificación 
df_limpio = pd.read_csv("01_datos/procesados/salarios_limpio.csv")

print(df_limpio.head())
print(df_limpio.shape)
print(df_limpio.columns)