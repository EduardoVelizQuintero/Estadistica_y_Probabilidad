# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 13: Estadistica no parametrica
# Ejercicio 13.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 13.1 - suma de rangos con empates
from scipy import stats
P = [8, 10, 10, 12]       # tiempos del quiosco P
Q = [10, 13, 14, 15]      # tiempos del quiosco Q
print(stats.rankdata(P + Q))          # el triple 10 recibe rango 3
print(stats.mannwhitneyu(P, Q))       # Mann-Whitney con empates
