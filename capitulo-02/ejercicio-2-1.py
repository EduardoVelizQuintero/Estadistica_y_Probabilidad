# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 2: Probabilidad
# Ejercicio 2.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 2.1 - Probabilidades de la suma de dos dados
# Se enumeran los 36 puntos muestrales y se cuentan

# itertools.product genera las 36 parejas (dado1, dado2)
from itertools import product
puntos = list(product(range(1, 7), repeat=2))

# len cuenta la lista: debe dar 36, el tamano de S
len(puntos)                       # 36

# La suma de cada pareja: la variable aleatoria
sumas = [a + b for a, b in puntos]

# Se cuentan los puntos favorables a cada evento
fav_7 = sum(1 for s in sumas if s == 7)        # 6
fav_10mas = sum(1 for s in sumas if s >= 10)  # 6

# Definicion ingenua: favorables / posibles
fav_7 / 36       # 0.16666666666666666  = 1/6
fav_10mas / 36   # 0.16666666666666666  = 1/6

# Counter reproduce la Figura 2.1: puntos por suma
from collections import Counter
sorted(Counter(sumas).items())
# [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6),
#  (8, 5), (9, 4), (10, 3), (11, 2), (12, 1)]
