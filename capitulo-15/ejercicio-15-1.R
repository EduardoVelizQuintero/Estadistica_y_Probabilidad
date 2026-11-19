# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 15: Distribuciones multivariantes
# Ejercicio 15.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 15.1 - Tabla conjunta 2 x 2
# X: 1 si paga con tarjeta; Y: 1 si compra fruta

# La tabla entra como matriz: filas X, columnas Y
p <- matrix(c(0.30, 0.10,
              0.20, 0.40),
            nrow = 2, byrow = TRUE)

# Control obligatorio: las celdas suman 1
sum(p)                            # 1

# Marginales: sumar hacia cada margen
pX <- rowSums(p)                  # 0.4 0.6
pY <- colSums(p)                  # 0.5 0.5

# Condicional P(Y = 1 | X = 1): celda entre marginal
p[2, 2] / pX[2]                   # 0.6666667

# Prueba de independencia en la celda (1, 1)
pX[2] * pY[2]                     # 0.30 esperado
p[2, 2]                           # 0.40 real: no independientes

# Esperanzas de variables 0-1: probabilidad del 1
ex <- pX[2]                       # 0.6
ey <- pY[2]                       # 0.5

# E(XY): solo la celda (1, 1) aporta
exy <- p[2, 2]                    # 0.4

# Covarianza por su forma de calculo
cov_xy <- exy - ex * ey
cov_xy                            # 0.1

# Varianzas 0-1 y correlacion
var_x <- ex - ex^2                # 0.24
var_y <- ey - ey^2                # 0.25
cov_xy / sqrt(var_x * var_y)      # 0.4082483
