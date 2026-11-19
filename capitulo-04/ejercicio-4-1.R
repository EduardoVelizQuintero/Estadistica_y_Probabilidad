# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 4: Variables aleatorias continuas y sus distribuciones de probabilidad
# Ejercicio 4.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 4.1 - Densidad f(x) = 3x^2 en (0, 1)
# La proporcion vendida antes del mediodia

# Se define la densidad como una funcion de x
f <- function(x) 3 * x^2

# Control obligatorio: el area total debe ser 1
integrate(f, 0, 1)$value          # 1

# La acumulada es F(x) = x^3: se escribe a mano
F_acum <- function(x) x^3

# Probabilidad de vender menos de la mitad
F_acum(0.5)                       # 0.125

# La misma probabilidad, integrando la densidad
integrate(f, 0, 0.5)$value        # 0.125

# Probabilidad entre 0.5 y 0.8: resta de acumuladas
F_acum(0.8) - F_acum(0.5)         # 0.387

# Esperanza: integral de x por f(x)
integrate(function(x) x * f(x), 0, 1)$value      # 0.75

# Segundo momento: integral de x^2 por f(x)
ex2 <- integrate(function(x) x^2 * f(x), 0, 1)$value
ex2                               # 0.6

# Varianza por la forma de calculo y desviacion
var_x <- ex2 - 0.75^2
var_x                             # 0.0375
sqrt(var_x)                       # 0.1936492
