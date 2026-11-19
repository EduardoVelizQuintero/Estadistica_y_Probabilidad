# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 7: Prueba de hipotesis
# Ejercicio 7.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 7.3 - Prueba Z para una proporcion (R)
phat <- 0.62; p0 <- 0.50; n <- 100
ee0 <- sqrt(p0 * (1 - p0) / n)   # 0.05, bajo H0
z <- (phat - p0) / ee0           # 2.4
2 * pnorm(z, lower.tail = FALSE)  # valor p: 0.0164

# En Python: 2 * stats.norm.sf(2.4)  # tambien 0.0164
