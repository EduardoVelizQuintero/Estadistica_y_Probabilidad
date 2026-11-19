# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.1 - Costo Y = 2X + 10, X uniforme en (1, 3)

# scipy.stats trae la uniforme y la normal
from scipy import stats

# Semilla y tamano de la simulacion
import numpy as np
rng = np.random.default_rng(2026)

# Densidad teorica de Y en 13: uniforme (12, 16)
print(stats.uniform.pdf(13, loc=12, scale=4))   # 0.25

# Probabilidad pedida: P(Y < 13)
print(stats.uniform.cdf(13, loc=12, scale=4))   # 0.25

# Media y varianza por las reglas lineales
media_y = 2 * 2 + 10              # 14
var_y = 4 * (2**2 / 12)           # 1.333...

# Comprobacion por simulacion
x = rng.uniform(1, 3, size=100000)  # distancias
y = 2 * x + 10                      # la transformacion
print(y.mean())                     # cerca de 14
print((y < 13).mean())             # cerca de 0.25
