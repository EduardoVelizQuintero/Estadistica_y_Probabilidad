# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.1 - Distribucion muestral de la media (R)
# Parametros de la poblacion y tamano de muestra
mu <- 80; sigma <- 24; n <- 36

# Error estandar: sigma / raiz(n) = 24 / 6 = 4
ee <- sigma / sqrt(n)

# P(Xbarra > 86) por el TLC: cola derecha de la normal
pnorm(86, mean = mu, sd = ee, lower.tail = FALSE)  # 0.0668

# Lo mismo estandarizando a mano: P(Z > 1.5)
pnorm(1.5, lower.tail = FALSE)                     # 0.0668

# P(76 < Xbarra < 84): area entre los dos valores
pnorm(84, mean = mu, sd = ee) - pnorm(76, mean = mu, sd = ee)  # 0.6827
