# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 2: Probabilidad
# Ejercicio 2.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 2.1 - Probabilidades de la suma de dos dados
# Se enumeran los 36 puntos muestrales y se cuentan

# expand.grid crea todas las parejas (dado1, dado2):
# 6 valores del primer dado por 6 del segundo = 36 filas
puntos <- expand.grid(dado1 = 1:6, dado2 = 1:6)

# nrow cuenta las filas: debe dar 36, el tamano de S
nrow(puntos)                      # 36

# Se crea la suma de cada pareja: la variable aleatoria
puntos$suma <- puntos$dado1 + puntos$dado2

# Se cuentan los puntos favorables a cada evento
fav_7    <- sum(puntos$suma == 7)      # 6 puntos
fav_10mas <- sum(puntos$suma >= 10)   # 6 puntos

# Definicion ingenua: favorables / posibles
fav_7 / 36       # 0.1666667  = 1/6
fav_10mas / 36   # 0.1666667  = 1/6

# table reproduce la Figura 2.1: puntos por cada suma
table(puntos$suma)
#  2  3  4  5  6  7  8  9 10 11 12
#  1  2  3  4  5  6  5  4  3  2  1
