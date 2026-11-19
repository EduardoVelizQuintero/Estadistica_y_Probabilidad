# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.2 - Tukey HSD tras el ANOVA
mejora <- c(10, 12, 14, 15, 17, 19, 11, 13, 12)
taller <- factor(rep(c("presencial", "virtual", "hibrido"), each = 3))
# dos parejas con diferencia 5 superan el HSD 4.34
TukeyHSD(aov(mejora ~ taller))
