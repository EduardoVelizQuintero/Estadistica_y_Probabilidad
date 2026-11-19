# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.2 - bondad de ajuste de un dado
import numpy as np
from scipy import stats
# conteos de las caras 1 a 6
observados = np.array([18, 22, 19, 21, 20, 20])
esperados = np.full(6, 20.0)  # 120 / 6 por cara si es justo
chi2 = ((observados - esperados) ** 2 / esperados).sum()
print(chi2, stats.chi2.sf(chi2, df=5))           # 0.50 ; p = 0.992
