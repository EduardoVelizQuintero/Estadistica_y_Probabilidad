# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.2 - La proporcion muestral, por el TLC
from scipy import stats  # trae la distribucion normal
# p = 0.30 en la poblacion; la encuesta entrevista n = 200
p, n = 0.30, 200
# Error estandar: raiz(p (1 - p) / n) = raiz(0.00105)
ee = (p * (1 - p) / n) ** 0.5  # 0.0324
# P(phat < 0.25): cola izquierda de la normal
print(stats.norm.cdf(0.25, loc=p, scale=ee))  # 0.0614
# P(phat > 0.36): sf es la cola derecha (survival)
print(stats.norm.sf(0.36, loc=p, scale=ee))  # 0.0320
