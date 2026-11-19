# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejercicio 5.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 5.1 - Distribucion muestral de la media (Python)
from scipy import stats  # trae la distribucion normal

# Parametros de la poblacion y tamano de muestra
mu, sigma, n = 80, 24, 36

# Error estandar: sigma / raiz(n) = 4
ee = sigma / n**0.5

# P(Xbarra > 86): sf es la cola derecha (survival)
print(stats.norm.sf(86, loc=mu, scale=ee))   # 0.0668

# P(76 < Xbarra < 84): diferencia de acumuladas
print(stats.norm.cdf(84, loc=mu, scale=ee)
      - stats.norm.cdf(76, loc=mu, scale=ee))  # 0.6827
