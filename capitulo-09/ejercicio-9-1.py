# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.1 - Otavalo: recta de minimos cuadrados
import numpy as np
# publicidad, cientos de dolares
x = np.array([1, 2, 3, 4, 5, 6], dtype=float)
# ventas, miles de dolares
y = np.array([12, 15, 17, 22, 24, 28], dtype=float)
Sxy = ((x - x.mean()) * (y - y.mean())).sum()    # suma cruzada: 56
Sxx = ((x - x.mean()) ** 2).sum()               # suma de x: 17.5
b1 = Sxy / Sxx                                  # pendiente: 3.20
b0 = y.mean() - b1 * x.mean()                   # ordenada: 8.47
print(b0, b1)                                   # recta ajustada
