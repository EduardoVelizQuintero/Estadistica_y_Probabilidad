# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 8: Propiedades de los estimadores puntuales y metodos de estimacion
# Ejercicio 8.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 8.3 - El sesgo del maximo, comprobado simulando (R)
set.seed(2026)                    # corrida reproducible
n <- 8; theta <- 12               # muestra de 8, theta verdadero 12
maximos <- replicate(10000, max(runif(n, 0, theta)))
mean(maximos)                     # cerca de 10.67: el sesgo se ve
mean(maximos) - theta             # cerca de -1.33
mean(maximos * (n + 1) / n)       # cerca de 12: corregido
