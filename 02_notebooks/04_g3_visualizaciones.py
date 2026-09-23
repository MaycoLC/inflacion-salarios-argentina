import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('01_datos/procesados/analisis_completo.csv', parse_dates=['fecha'])

fig, ax = plt.subplots(figsize=(14,5))

ax.plot(df['fecha'], df['salario_real_total'], color='#1A3A5C', linewidth=2.5, label='Total', linestyle='--')

ax.plot(df['fecha'], df['salario_real_priv_reg'], color='#2E6DA4', linewidth=1.8, label='Privado registrado)')

ax.plot(df['fecha'], df['salario_real_publico'], color='#1D9E75', linewidth=1.8, label='Sector público')

# Línea base = 100 (nivel de partida)

ax.axhline(y=100, color='gray', linestyle=':', linewidth=1, label='Nivel base 2017')

ax.set_title('Salario real por sector · Argentina 2017/2024\n (poder adquisitivo real)',
            fontsize=14, fontweight='bold', pad=15)

ax.set_xlabel('Período', fontsize=11)
ax.set_ylabel('Índice de salario real (base 100)', fontsize=11)
ax.legend(fontsize=10)
ax.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('04_outputs/G3_salario_real_sectores.png', dpi=150, bbox_inches='tight')
plt.show()
