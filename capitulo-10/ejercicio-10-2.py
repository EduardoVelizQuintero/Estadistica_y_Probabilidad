# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.2 - Tukey HSD tras el ANOVA
from statsmodels.stats.multicomp import pairwise_tukeyhsd
mejora = [10, 12, 14, 15, 17, 19, 11, 13, 12]
taller = (["presencial"] * 3 + ["virtual"] * 3 + ["hibrido"] * 3)
# virtual difiere de ambos
print(pairwise_tukeyhsd(mejora, taller, alpha=0.05))
