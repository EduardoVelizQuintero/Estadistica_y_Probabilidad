# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.2 - La proporcion muestral, por el TLC
# p = 0.30 en la poblacion; la encuesta entrevista n = 200
p <- 0.30; n <- 200
# Error estandar: raiz(p (1 - p) / n) = raiz(0.00105)
ee <- sqrt(p * (1 - p) / n)  # 0.0324
# P(phat < 0.25): cola izquierda de la normal
pnorm(0.25, mean = p, sd = ee)  # 0.0614
# P(phat > 0.36): cola derecha de la normal
pnorm(0.36, mean = p, sd = ee, lower.tail = FALSE)  # 0.0320
