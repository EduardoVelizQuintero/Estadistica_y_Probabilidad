# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.1 - Otavalo: recta de minimos cuadrados
x <- c(1, 2, 3, 4, 5, 6)          # publicidad, cientos de dolares
y <- c(12, 15, 17, 22, 24, 28)    # ventas, miles de dolares
ajuste <- lm(y ~ x)  # ajusta y = b0 + b1 x por minimos cuadrados
coef(ajuste)                      # b0 = 8.47 ; b1 = 3.20
summary(ajuste)$r.squared         # R2 del ajuste
