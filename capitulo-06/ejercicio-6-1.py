# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 6: Estimacion
# Ejercicio 6.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 6.1 - Intervalo para una media (Python)
# El mismo procedimiento de R, paso a paso, en otro lenguaje.

import numpy as np            # numpy: calculo numerico con vectores
from scipy import stats       # stats: distribucion t de Student

gasto = np.array([68, 72, 75, 80, 82, 85,   # los 12 gastos, en dolares
                  88, 90, 94, 98, 105, 112]) # como arreglo numerico
n = len(gasto)                # n = 12: tamano de la muestra
media = gasto.mean()          # media muestral: estimacion puntual
s = gasto.std(ddof=1)         # desviacion muestral: ddof=1 divide entre n-1
error_std = s / np.sqrt(n)    # error estandar de la media
t_crit = stats.t.ppf(0.975, df=n-1)  # critico t: 95%, 11 grados de libertad
margen = t_crit * error_std   # margen de error del intervalo
ic_inf = media - margen       # limite inferior: 78.99
ic_sup = media + margen       # limite superior: 95.84
print(f"Media: {media:.2f}")  # imprime la media con 2 decimales: 87.42
print(f"IC 95%: {ic_inf:.2f} a {ic_sup:.2f}")  # imprime el intervalo

# Comprobacion con la funcion directa:
print(stats.t.interval(0.95, df=n-1,  # intervalo t al 95%
                       loc=media,     # centrado en la media muestral
                       scale=error_std))  # con su error estandar
