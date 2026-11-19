# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.2 - contraste para la correlacion
import numpy as np
from scipy import stats
r, n = 0.75, 10                             # correlacion y muestra
t = r * np.sqrt(n - 2) / np.sqrt(1 - r**2)  # estadistico t: 3.21
p = 2 * stats.t.sf(abs(t), df=n - 2)        # valor p bilateral
print(t, p)                                 # 3.21 ; 0.0125
