# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.3 - Una varianza muestral con la chi cuadrado
from scipy import stats  # trae la distribucion chi cuadrado
# Estadistico: (n - 1) S2 / sigma2, con n = 11 quesos
print((11 - 1) * 625 / 20**2)  # 15.625
# Percentil 95 de la chi cuadrado con 10 grados
print(stats.chi2.ppf(0.95, 10))  # 18.307: no lo supera
# P(chi2 con 10 g. l. > 15.625): sf es la cola derecha
print(stats.chi2.sf(15.625, 10))  # 0.1109
