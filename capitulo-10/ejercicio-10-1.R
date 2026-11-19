# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.1 - ANOVA de un factor en R
mejora <- c(10, 12, 14, 15, 17, 19, 11, 13, 12)   # puntos de mejora
taller <- factor(rep(c("presencial", "virtual", "hibrido"), each = 3))
summary(aov(mejora ~ taller))   # F = 8.33 ; p = 0.019
