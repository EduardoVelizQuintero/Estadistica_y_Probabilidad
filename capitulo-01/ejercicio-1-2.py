# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 1: Que es estadistica?
# Ejercicio 1.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 1.2 en Python: el mismo contraste
import numpy as np                      # numpy: media y mediana
comisiones = np.array([320, 340, 350, 360, 370, 380, 390, 400, 850])
print(comisiones.mean())                # media con el atipico: 417.78
print(np.median(comisiones))            # mediana: 370.0
