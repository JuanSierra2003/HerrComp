# Tutorial: Uso del Notebook para el Modelo de Vegetación, Presas y Depredadores

## Introducción

Este documento presenta un tutorial detallado en español para entender y utilizar el notebook que implementa un modelo de interacción ecológica. En este notebook se simulan dos modelos:

- **Modelo Lotka–Volterra**: Considera la interacción entre presas y depredadores.
- **Modelo Extendido**: Incorpora además la dinámica de la vegetación.

Asimismo, se incluye un análisis de estabilidad a través del cálculo del Jacobiano y la evaluación de sus valores propios.

## Requerimientos e Instalación

Antes de ejecutar el notebook, asegúrate de tener instaladas las siguientes librerías de Python:

- **NumPy**: Para operaciones matemáticas y manejo de arrays.
- **Matplotlib**: Para la generación de gráficos.
- **SciPy**: Para resolver ecuaciones diferenciales y calcular valores propios.

Si aún no las tienes, instálalas utilizando `pip`:

```bash
pip install numpy matplotlib scipy
