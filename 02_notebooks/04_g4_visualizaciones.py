import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('01_datos/procesados/analisis_completo.csv', parse_dates=['fecha'])



# Agrupar por año y calcular inflación anual.
df['anio'] = df['fecha'].dt.year
ipc_anual = df.groupby('anio')['ipc_variacion_mensual'].apply(
    lambda x: ((1 + x/100).prod() - 1) * 100
).reset_index()
ipc_anual.columns = ['anio', 'inflacion_anual']

fig, ax = plt.subplots(figsize=(14,5))

colores = ['#D6E4F0' if v < 50 else '#2E6DA4' if v < 100 else '#1A3A5C'
           for v in ipc_anual['inflacion_anual']]

bars = ax.bar(ipc_anual['anio'].astype(str), ipc_anual['inflacion_anual'], color=colores, edgecolor='white')

# Etiquetas sobre cada barra

for bar, val in zip(bars, ipc_anual['inflacion_anual']):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
        f'{val:.0f}%', ha='center', va='bottom', fontsize=8, fontweight='bold')

ax.set_title('Inflación anual en Argentina · 2017-2024',
             fontsize=14, fontweight='bold', pad=15)

ax.set_xlabel('Año', fontsize=11)
ax.set_ylabel('Inflación anual (%)', fontsize=11)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('04_outputs/G4_inflacion_anual.png', dpi=150, bbox_inches='tight')
plt.show()