# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.1 - beta-binomial con a priori uniforme
from scipy import stats
a_post, b_post = 1 + 3, 1 + (10 - 3)   # a posteriori Beta(4, 8)
print(a_post / (a_post + b_post))      # media a posteriori: 0.33
# creible: 0.11 a 0.61
print(stats.beta.ppf([0.025, 0.975], a_post, b_post))
