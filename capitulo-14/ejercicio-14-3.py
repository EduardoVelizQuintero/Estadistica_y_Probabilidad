# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.3 - probabilidad a posteriori sobre el parametro
from scipy import stats
# A posteriori: mu ~ Normal(534.48, 18.57)
# P(mu > 520 | datos) = 0.78
print(stats.norm.sf(520, loc=534.48, scale=18.57))
print(stats.norm.cdf(560, 534.48, 18.57)
      - stats.norm.cdf(500, 534.48, 18.57))  # P(500 < mu < 560) = 0.88
