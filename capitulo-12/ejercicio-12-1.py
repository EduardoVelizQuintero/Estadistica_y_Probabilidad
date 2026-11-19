# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.1 - chi cuadrado en una tabla 2 x 2
import numpy as np
from scipy import stats
tabla = np.array([[40, 20], [30, 30]])  # filas: genero ; columnas: compra
chi2, p, gl, esperados = stats.chi2_contingency(tabla, correction=False)
print(chi2, p, gl)                           # 3.43 ; 0.064 ; 1
print(esperados)                             # 35, 25 ; 35, 25
