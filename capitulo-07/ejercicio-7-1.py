# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 7: Prueba de hipotesis
# Ejercicio 7.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 7.1 - Prueba Z bilateral para una media (Python)
from scipy import stats  # trae la normal

# Datos y protocolo: H0 mu = 500, bilateral, alfa 0.05
xbarra, mu0, sigma, n = 515, 500, 70, 49

# Error estandar y estadistico
ee = sigma / n**0.5             # 10.0
z = (xbarra - mu0) / ee         # 1.5

# Critico bilateral y valor p (sf = cola derecha)
print(stats.norm.ppf(0.975))    # 1.96
print(2 * stats.norm.sf(z))     # 0.1336
