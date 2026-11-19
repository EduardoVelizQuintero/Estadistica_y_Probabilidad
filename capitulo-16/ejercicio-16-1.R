# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.1 - Costo Y = 2X + 10, X uniforme en (1, 3)
# Todo el codigo usa solo la distribucion de X

# Densidad teorica de Y: uniforme en (12, 16), altura 1/4
dunif(13, min = 12, max = 16)      # 0.25

# Probabilidad pedida: P(Y < 13)
punif(13, min = 12, max = 16)     # 0.25

# Media y varianza por las reglas de la transformacion lineal
media_y <- 2 * 2 + 10             # E(Y) = 2 E(X) + 10 = 14
var_y <- 4 * (2^2 / 12)           # Var(Y) = 4 Var(X) = 1.333...

# Comprobacion por simulacion: transformar valores de X
set.seed(2026)                    # semilla: resultado reproducible
x <- runif(100000, min = 1, max = 3)  # distancias simuladas
y <- 2 * x + 10                   # la transformacion, tal cual
mean(y)                           # cerca de 14
mean(y < 13)                      # cerca de 0.25
