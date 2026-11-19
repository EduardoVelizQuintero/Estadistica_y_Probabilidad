# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.2 - bondad de ajuste de un dado
observados <- c(18, 22, 19, 21, 20, 20)   # conteos de las caras 1 a 6
chisq.test(observados, p = rep(1/6, 6))   # chi2 = 0.50 ; gl = 5 ; p = 0.992
