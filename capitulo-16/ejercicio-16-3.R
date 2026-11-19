# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 16: Funciones de variables aleatorias
# Ejercicio 16.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 16.3 - Minimo de 4 exponenciales de media 8
# El minimo es exponencial de media 8 / 4 = 2 horas
# P(minimo > 2) = e^-1: 2 horas sin detenerse
pexp(2, rate = 1/2, lower.tail = FALSE)  # 0.3679
# P(minimo < 1) = 1 - e^-0.5
pexp(1, rate = 1/2)  # 0.3935
# Comprobacion por simulacion: el minimo de cada fila
set.seed(2026)  # semilla: resultado reproducible
fallas <- matrix(rexp(4 * 10000, rate = 1/8), ncol = 4)
minimos <- apply(fallas, 1, min)  # primera falla por turno
mean(minimos)  # cerca de 2 horas
mean(minimos > 2)  # cerca de 0.3679
