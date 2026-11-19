# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.1 - ANOVA de un factor en Python
from scipy import stats
presencial = [10, 12, 14]   # media 12
virtual = [15, 17, 19]      # media 17
hibrido = [11, 13, 12]      # media 12
F, p = stats.f_oneway(presencial, virtual, hibrido)
print(F, p)                 # F = 8.33 ; p = 0.019
