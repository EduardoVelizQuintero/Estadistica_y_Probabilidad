# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 13: Estadistica no parametrica
# Ejercicio 13.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 13.1 - suma de rangos con empates
P <- c(8, 10, 10, 12)     # tiempos del quiosco P
Q <- c(10, 13, 14, 15)    # tiempos del quiosco Q
rank(c(P, Q))             # el triple 10 recibe el rango promedio 3
wilcox.test(P, Q)         # suma de rangos con correccion por empates
