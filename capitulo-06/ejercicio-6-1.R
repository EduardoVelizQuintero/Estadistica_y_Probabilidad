# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 6: Estimacion
# Ejercicio 6.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 6.1 - Intervalo para una media (R)
# Cada linea se comenta para poder leer el codigo como texto.

gasto <- c(68, 72, 75, 80, 82, 85,   # guarda los 12 gastos en un vector
           88, 90, 94, 98, 105, 112) # en dolares por semana
n <- length(gasto)          # n = 12: el tamano de la muestra
media <- mean(gasto)        # media muestral: la estimacion puntual
s <- sd(gasto)              # desviacion estandar muestral (usa n-1)
error_std <- s / sqrt(n)    # error estandar de la media: s / raiz(n)
# valor critico t: 95% y 11 grados de libertad
t_crit <- qt(0.975, df = n - 1)
margen <- t_crit * error_std    # margen de error: critico x error estandar
ic_inf <- media - margen    # limite inferior del intervalo
ic_sup <- media + margen    # limite superior del intervalo
cat("Media:", media, "\n")  # imprime la estimacion puntual: 87.42
# imprime el intervalo: 78.99 a 95.84
cat("IC 95%:", ic_inf, "a", ic_sup, "\n")

# Comprobacion con la funcion directa de R:
t.test(gasto, conf.level = 0.95)  # debe dar el mismo intervalo
# t.test aplica exactamente este procedimiento:
# media, t con n-1 grados de libertad y nivel fijado.
