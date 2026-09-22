import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('01_datos/procesados/analisis_completo.csv', parse_dates=['fecha'])

fig, ax = plt.subplots(figsize=(14,5))

ax.bar(df['fecha'], df['ipc_variacion_mensual'], color='#2E6DA4', alpha=0.8)

# Línea de referencia en 5% mensual.

ax.axhline(y=5, color='#E07020', linestyle='--', linewidth=1.2, label='5% mensual')

ax.set_title('Inflación mensual en Argentina · 2017-2024', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Período', fontsize=11)
ax.set_ylabel('Variación mensual (%)', fontsize=11)
ax.legend()
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('04_outputs/G1_inflacion_mensual.png', dpi=150, bbox_inches='tight')
plt.show()
print('Gráfico 1 guardado.')

