# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.2 - Estandarizar X ~ N(90, 12)
# Y = (X - 90) / 12 es normal estandar N(0, 1)
# P(Y < 1.25): el viaje dura menos de 105 minutos
pnorm(1.25)  # 0.8944
# P(-1 < Y < 1): la masa central de la estandar
pnorm(1) - pnorm(-1)  # 0.6827
# Comprobacion directa con X, sin estandarizar
pnorm(105, mean = 90, sd = 12)  # 0.8944: la misma cuenta
