# Evolución del Poder Adquisitivo · Argentina (2017-2024)

### La carrera de los precios: el impacto de la inflación en el salario real

Índice de Precios al Consumidor - Índice de Salarios

**Fuente:** INDEC · Datos públicos de Argentina · Secretaría de Trabajo

**Etapas completadas:** Python (Pandas/Matplotlib) · Tableau 

\---

## Contexto y Definiciones

Este proyecto analiza la dinámica entre la inflación (Índice de Precios al Consumidor) y los salarios en Argentina durante un período de alta volatilidad macroeconómica (2017-2024).

* **Pérdida Adquisitiva:** Representada visualmente como la brecha o área de diferencia entre la evolución acumulada de la inflación y la evolución del índice general de salarios.   

* **Salario Real:** Es el poder de compra del salario. Se calcula ajustando el salario nominal por la inflación del mismo período. Si la inflación supera al aumento salarial, el salario real cae.

\---

## Preguntas que responde este análisis 

* ¿En qué momento se produjo el quiebre donde los salarios comenzaron a perder sistemáticamente contra la inflación?
* ¿Qué sector productivo (público vs. privado registrado) logró defender mejor su poder de compra?
* ¿Cuáles fueron los picos históricos de inflación interanual y mensual en el período analizado?
* ¿En qué período intercensal fue más acelerado el proceso de envejecimiento?

\---

## Hallazgos principales

* **Caída generalizada del poder de compra:** Tomando como base 100 el año 2017, todos los sectores sufrieron una severa contracción de su salario real, ubicándose por debajo del nivel base de manera ininterrumpida desde mediados de 2018.
* **Disparidad por sector:** El **Sector Privado Registrado** mostró mayor resistencia, rebotando hacia un índice aproximado de 85 a mediados de 2024. En contraste, el **Sector Público** fue el m+as castigado, tocando un piso histórico cercano a los 63 puntos a principios de 2024.
* **Picos inflacionarios históricos:** La variación interanual máxima del IPC alcanzó su pico más drástico en **2023 con un 211,2%**, seguido de cerca por las métricas obtenidas a principios de 2024 (117,4%).
* **Aceleración mensual:** El desglose trimestral/mensual evidencia que a finales de 2023 y principios de 2024 concentraron las variaciones mensuales más extremas, superando los 20 puntos porcentuales en un solo período.
* **Brecha exponencial:** La curva acumulada del IPC muestra un comportamiento de crecimiento exponencial a partir de 2022, dejando al índice salarial general rezagado y generando una zona de "pérdida adquisitiva" masiva. 

\---

## Datos utilizados | 1. IPC - Índice de Precios al Consumidor 

|Campo|Detalle|
|-|-|
|Fuente original|INDEC · Sociedad · Trabajo e ingresos · Salarios|
|Archivo|Serie histórica IPC Nacional|
|Formato|Excel (.xls)|
|Frecuencia|Mensual|
|Variable clave|Variación mensual e índice base 100 = diciembre 2016|
|Cobertura|Nacional, GBA, Pampeana, NOA, NEA, Cuyo, Patagonia|

## Datos utilizados | 2. Índice de Salarios 

|Campo|Detalle|
|-|-|
|Fuente original|INDEC · Economía · Precios · IPC Nacional|
|Archivo|Serie histórica de Índice de Salarios|
|Formato|Excel (.xls)|
|Frecuencia|Mensual|
|Variable clave|Variación mensual e índice base 100 = diciembre 2016|
|Cobertura|Nacional, GBA, Pampeana, NOA, NEA, Cuyo, Patagonia|

\---

## Etapa 1 · Python

### Limpieza y Análisis 

**Procesamiento de datos:** 
Uso de la librería `pandas` para la ingesta de archivos CSV. Se resolvieron inconsistencias de formato regional (conversión de comas decimales a puntos) y se normalizaron los tipos de datos temporales (fechas).

**Cálculo de métricas:** 
Generación de las columnas de variación real y acumulada. Diferenciación técnica entre picos interanuales y valores de cierre a diciembre mediante agrupaciones (`groupby` y agregaciones).

**Prototipado visual:**  
Uso de `matplotlib` para establecer la lógica visual (uso de `fill_between` para el sombreado de la brecha adquisitiva, ajustes de transparencia con `alpha`, y renderizado de ejes duales).

### Scripts disponibles

|Archivo|Descripción|
|-|-|
|`04_notebooks\01_limpiar_ipc.py`|Script de limpieza del IPC.|
|`04_notebooks\02_limpiar_ind_salario.py`|Script de limpieza del Índice de Salarios.|
|`04_notebooks\03_analisis.py`|Script de análisis con pandas de ambos .csv procesados.|
|`04_notebooks\04_g1_visualizaciones.py`|Script de inflación mensual 2017 - 2024.|
|`04_notebooks\04_g2_visualizaciones.py`|Script de inflación acumulada vs. salarios.|
|`04_notebooks\04_g3_visualizaciones.py`|Script de salario real por sector.|
|`04_notebooks\04_g3_visualizaciones.py`|Script de inflación anual comparada.|

\---

## Estructura del repositorio

```
inflacion-salarios-argentina/
├── 01_datos/
│   ├── original/
|   |   └── indice_salarios.xls    ← INDEC sin modificar
│   │   └── ipc_nacional.xls    ← INDEC sin modificar
│   └── procesados/
│       └── analisis_completo.csv      ← dataset limpio
|       └── ipc_limpio.csv      
|       └── salarios_limpio.csv      
├── 02_notebooks/
│   └── 01_limpiar_ipc.py
│   └── 02_limpiar_ind_salario.py
│   └── 03_analisis.py
│   └── 04_g1_visualizaciones.py
│   └── 04_g2_visualizaciones.py
│   └── 04_g3_visualizaciones.py
│   └── 04_g4_visualizaciones.py
├── 03_capturas/
│   └── CP01_setup_python.png
│   └── CP02_dataframe_ipc_limpio.png
│   └── CP03_dataframe_indice_salario_limpio.png
│   └── CP04_analisis_pandas.png
│   └── CP05_dashboard_tableau.png
├── 04_outputs/
│   └── G1_inflacion_mensual.png
│   └── G2_ipc_vs_salarios.png
│   └── G3_salarios_real_sectores.png
│   └── G4_inflacion_anual.png
├── venv/   ← entorno virtual
└── README.md
```

\---

### Visualizaciones

|Gráfico|Tipo|Pregunta que responde|
|-|-|-|
|Inflación anual|Barras con color por escala|¿Qué año sufrió mayor inflación?|
|IPC vs Salarios|Líneas duales con área|¿Cuándo la inflación superó a los salarios?|
|Inflación mensual|Barras verticales|¿En qué meses subieron más los precios?|
|Salario real por sector|Líneas múltiples|¿Qué sector conservó más poder adquisitivo?|

Los gráficos pueden ser generados mediante los scripts de Python mencionados o visualizados mediante Tableau Public en mi perfil.

\---

### Etapa 3 · Tableau

Dashboard interactivo conectado al CSV generado por el script 03. Incluye todas las visualizaciones mencionadas con la posibilidad de interactuar con las mismas. Se encuentra publicado en Tableau Public en el siguiente link:

https://public.tableau.com/views/InflacinySalariosenArgentinaMaycoCorrea/Presentacin?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

\---

## Herramientas utilizadas

![Excel](https://img.shields.io/badge/Microsoft\_Excel-217346?style=flat\&logo=microsoft-excel\&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-007ACC?style=flat&logo=visual-studio-code&logoColor=white)
![Tableau](https://img.shields.io/badge/Tableau-E97627?style=flat&logo=tableau&logoColor=white)

\---

*Proyecto de portafolio de análisis de datos · Etapas 1 y 2 completadas*

