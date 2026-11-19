# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.2 - efectos de un factorial 2 x 2
import numpy as np
# filas: riego; cols: fertilizante
c = np.array([[38, 44], [47, 61]], dtype=float)
print(c[1].mean() - c[0].mean())   # efecto riego: +13
print(c[:, 1].mean() - c[:, 0].mean())  # efecto fertilizante: +10
print((c[1, 1] - c[1, 0]) - (c[0, 1] - c[0, 0]))  # interaccion: +8
