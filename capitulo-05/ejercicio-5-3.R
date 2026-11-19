# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.3 - Una varianza muestral con la chi cuadrado
# Estadistico: (n - 1) S2 / sigma2, con n = 11 quesos
(11 - 1) * 625 / 20^2  # 15.625
# Percentil 95 de la chi cuadrado con 10 grados
qchisq(0.95, df = 10)  # 18.307: 15.625 no lo supera
# P(chi2 con 10 g. l. > 15.625): la probabilidad pedida
pchisq(15.625, df = 10, lower.tail = FALSE)  # 0.1109
