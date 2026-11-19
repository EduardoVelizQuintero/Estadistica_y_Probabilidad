# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.3 - ANOVA como regresion con indicadoras
ventas <- c(210, 230, 225, 215, 240, 255, 250, 245, 195, 205, 200, 210)
sucursal <- factor(rep(c("Centro", "Norte", "Sur"), each = 4))
summary(lm(ventas ~ sucursal))  # R2 = 0.892 ; F = 37.05 : el mismo ANOVA
