# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.2 - Estandarizar X ~ N(90, 12)
from scipy import stats  # trae la distribucion normal
# Y = (X - 90) / 12 es normal estandar N(0, 1)
# P(Y < 1.25): el viaje dura menos de 105 minutos
print(stats.norm.cdf(1.25))  # 0.8944
# P(-1 < Y < 1): diferencia de acumuladas
print(stats.norm.cdf(1) - stats.norm.cdf(-1))  # 0.6827
# Comprobacion directa con X, sin estandarizar
print(stats.norm.cdf(105, loc=90, scale=12))  # 0.8944
