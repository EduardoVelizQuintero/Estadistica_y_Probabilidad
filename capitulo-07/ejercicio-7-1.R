# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 7: Prueba de hipotesis
# Ejercicio 7.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 7.1 - Prueba Z bilateral para una media (R)
# Protocolo: H0 mu = 500, Ha mu != 500, alfa = 0.05
xbarra <- 515; mu0 <- 500; sigma <- 70; n <- 49

# Error estandar y estadistico
ee <- sigma / sqrt(n)           # 10
z <- (xbarra - mu0) / ee        # 1.5

# Valor critico bilateral al 5 por ciento
qnorm(0.975)                    # 1.96: |z| no lo alcanza

# Valor p bilateral: el doble de la cola derecha
2 * pnorm(z, lower.tail = FALSE)  # 0.1336
