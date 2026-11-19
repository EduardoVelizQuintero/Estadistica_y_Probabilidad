# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 13: Estadistica no parametrica
# Ejercicio 13.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 13.2 - rangos con signo con una diferencia cero
antes <- c(9, 7, 12, 8, 10)     # errores antes de la capacitacion
despues <- c(6, 7, 9, 5, 8)     # errores despues
# excluye el par con diferencia 0
wilcox.test(antes, despues, paired = TRUE)
