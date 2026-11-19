# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 3: Variables aleatorias discretas y sus distribuciones de probabilidad
# Ejercicio 3.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 3.1 - Esperanza y varianza de las entregas
# Tabla del enunciado: conteos y sus probabilidades

# Los valores posibles de X: entregas por hora
x <- c(0, 1, 2, 3)

# La funcion de probabilidad p(x), en el mismo orden
p <- c(0.20, 0.40, 0.30, 0.10)

# Control obligatorio: las probabilidades suman 1
sum(p)                            # 1

# Esperanza: suma de x por p(x), termino a termino
mu <- sum(x * p)
mu                                # 1.3

# Segundo momento: suma de x^2 por p(x)
ex2 <- sum(x^2 * p)
ex2                               # 2.5

# Varianza por la forma de calculo: E(X^2) - mu^2
var_x <- ex2 - mu^2
var_x                             # 0.81
sqrt(var_x)                       # 0.9

# El ingreso es g(X) = 3X: se aplica sobre la misma tabla
ingreso <- 3 * x
sum(ingreso * p)                  # 3.9 dolares por hora
3 * sqrt(var_x)                   # 2.7 dolares de desviacion
