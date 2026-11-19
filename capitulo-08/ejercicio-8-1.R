# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 8: Propiedades de los estimadores puntuales y metodos de estimacion
# Ejercicio 8.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 8.1 - Eficiencia relativa (R)
sigma <- 12                     # desviacion poblacional
var_a <- sigma^2                # Var(X1) = 144
var_b <- sigma^2 / 2            # Var de la media de 2 = 72
var_c <- sigma^2 / 3            # Var de la media de 3 = 48

# Eficiencias respecto de A: cociente de varianzas
var_a / var_b                   # 2
var_a / var_c                   # 3

# Desviaciones estandar de cada regla, en dolares
sqrt(c(var_a, var_b, var_c))    # 12.00, 8.49, 6.93
