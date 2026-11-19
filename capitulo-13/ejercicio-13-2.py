# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 13: Estadistica no parametrica
# Ejercicio 13.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 13.2 - rangos con signo con una diferencia cero
from scipy import stats
antes = [9, 7, 12, 8, 10]       # errores antes de la capacitacion
despues = [6, 7, 9, 5, 8]       # errores despues
print(stats.wilcoxon(antes, despues))  # el par con diferencia 0 se excluye
