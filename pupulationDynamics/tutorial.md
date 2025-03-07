# Tutorial Práctico: Simulación de Dinámicas Ecológicas con `Vegetacion.ipynb`  

Este código modela la interacción entre vegetación, presas y depredadores usando ecuaciones diferenciales. **Pasos para usarlo**:  

1. **Prepara el entorno**:  
   - Asegúrate de tener instaladas las bibliotecas `numpy`, `matplotlib` y `scipy`. Si no las tienes, instálalas con:  
     ```bash  
     pip install numpy matplotlib scipy  
     ```  

2. **Modifica parámetros (opcional)**:  
   - Los valores predeterminados están definidos al inicio (ej: `alpha = 0.8`, `beta = 0.05`). Cámbialos según el escenario que quieras simular. Por ejemplo:  
     - Aumentar `alpha` acelera el crecimiento de la vegetación.  
     - Reducir `zeta` ralentiza el crecimiento de depredadores.  

3. **Ejecuta el código**:  
   - Al correr todo el script (en un entorno como Jupyter Notebook o Python), se calculan dos modelos:  
     - **Modelo clásico Lotka-Volterra**: Solo presas (`P`) y depredadores (`D`), con vegetación constante.  
     - **Modelo extendido**: Incluye la dinámica de vegetación (`V`).  

4. **Resultados gráficos**:  
   - Se generan dos imágenes:  
     - **`Lotka_Volterra.png`**: Muestra la evolución temporal de las poblaciones.  
       - **Líneas continuas**: Modelo extendido (vegetación + presas + depredadores).  
       - **Líneas discontinuas (`--`)**: Modelo clásico (solo presas y depredadores).  
       - **Líneas punteadas (`:`)**: Valores de equilibrio teóricos.  
     - **`stability.png`**: Mapa de estabilidad de los puntos de equilibrio (regiones violeta = estables, celeste = inestables).  

5. **Personaliza la simulación**:  
   - **Cambia el tiempo de simulación**: Modifica `t_span = (0, 1500)` para acortar o extender el periodo.  
   - **Ajusta la resolución**: Usa `t_eval = np.linspace(*t_span, 1000)` (a mayor número, más puntos).  
   - **Modifica condiciones iniciales**: Edita `V0, P0, D0 = alpha/gamma, 5, 2`.  

6. **Interpreta las gráficas**:  
   - **Oscilaciones**: Indican ciclos naturales entre presas y depredadores.  
   - **Convergencia a líneas punteadas**: El sistema alcanza equilibrio estable.  
   - **Caos o divergencia**: Parámetros no balanceados (requiere ajustar valores como `beta` o `epsilon`).  

**Nota**: El análisis de estabilidad (`stability.png`) usa la matriz Jacobiana para evaluar si pequeños cambios en las poblaciones se amortiguan (estable) o crecen (inestable). Para profundizar, modifica las funciones `jacobian` y `stability` al final del código.  
