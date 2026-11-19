# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.3 - Minimo de 4 exponenciales de media 8
from scipy import stats  # trae la distribucion exponencial
import numpy as np  # matrices para la simulacion
# El minimo es exponencial de media 8 / 4 = 2 horas
# P(minimo > 2) = e^-1: sf es la cola derecha
print(stats.expon.sf(2, scale=2))  # 0.3679
# P(minimo < 1) = 1 - e^-0.5
print(stats.expon.cdf(1, scale=2))  # 0.3935
# Comprobacion por simulacion: el minimo de cada fila
rng = np.random.default_rng(2026)  # semilla reproducible
fallas = rng.exponential(scale=8, size=(10000, 4))
minimos = fallas.min(axis=1)  # primera falla por turno
print(minimos.mean())  # cerca de 2 horas
print((minimos > 2).mean())  # cerca de 0.3679
