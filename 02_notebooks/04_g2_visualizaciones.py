import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('01_datos/procesados/analisis_completo.csv', parse_dates=['fecha'])

fig, ax = plt.subplots(figsize=(14,5))

ax.plot(df['fecha'], df['ipc_acumulado'], color='#E07020', linewidth=2.5, label='IPC (inflación)')
ax.plot(df['fecha'], df['salario_total'], color='#1A3A5C', linewidth=2, label='Salarios (índice general)')

ax.fill_between(df['fecha'], df['ipc_acumulado'], df['salario_total'], 
                where=(df['ipc_acumulado'] > df['salario_total']),
                alpha=0.2, color='red', label='Pérdida de poder adquisitivo.'
                )

ax.set_title('Inflación vs. Salarios · Argentina 2017–2024\n(base 100 = dic 2016)',
            fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Período', fontsize=11)
ax.set_ylabel('Índice (base 100)', fontsize=11)
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('04_outputs/G2_ipc_vs_salarios.png', dpi=150, bbox_inches='tight')
plt.show()