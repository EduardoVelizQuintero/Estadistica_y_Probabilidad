# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.3 - esperados pequenos: prueba exacta de Fisher
import numpy as np
from scipy import stats
tabla = np.array([[8, 2], [4, 6]])  # filas: tratamiento ; columnas: mejoria
esperados = stats.chi2_contingency(tabla, correction=False)[3]
print(esperados)  # 6, 4 ; 6, 4 : dos celdas bajo 5
odds, p = stats.fisher_exact(tabla)           # prueba exacta de Fisher
print(p)  # valor p exacto, sin aproximacion
