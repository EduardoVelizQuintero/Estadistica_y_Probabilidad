# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.2 - Poisson-gamma conjugada
from scipy import stats
forma_post, tasa_post = 8 + 18, 2 + 3   # a posteriori Gamma(26, 5)
print(forma_post / tasa_post)           # media a posteriori: 5.2 por hora
# 3.40 a 7.38
print(stats.gamma.ppf([0.025, 0.975], a=forma_post, scale=1 / tasa_post))
