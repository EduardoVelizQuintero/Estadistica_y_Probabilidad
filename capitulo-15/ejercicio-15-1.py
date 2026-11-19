# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 15: Distribuciones multivariantes
# Ejercicio 15.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 15.1 - Tabla conjunta 2 x 2
# X: 1 si paga con tarjeta; Y: 1 si compra fruta

# numpy trabaja con arreglos numericos
import numpy as np

# La tabla entra como matriz: filas X, columnas Y
p = np.array([[0.30, 0.10],
              [0.20, 0.40]])

# Control obligatorio: las celdas suman 1
print(p.sum())                    # 1.0

# Marginales: sumar por filas y por columnas
pX = p.sum(axis=1)                # [0.4 0.6]
pY = p.sum(axis=0)                # [0.5 0.5]

# Condicional P(Y = 1 | X = 1): celda entre marginal
print(p[1, 1] / pX[1])            # 0.6666...

# Prueba de independencia en la celda (1, 1)
print(pX[1] * pY[1])              # 0.30 esperado
print(p[1, 1])                    # 0.40 real

# Esperanzas de variables 0-1
ex = pX[1]                        # 0.6
ey = pY[1]                        # 0.5

# E(XY): solo la celda (1, 1) aporta
exy = p[1, 1]                     # 0.4

# Covarianza por su forma de calculo
cov_xy = exy - ex * ey
print(cov_xy)                     # 0.1 (salvo redondeo)

# Varianzas 0-1 y correlacion
var_x = ex - ex**2                # 0.24
var_y = ey - ey**2                # 0.25
print(cov_xy / np.sqrt(var_x * var_y))  # 0.4082...
