# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.3 - prediccion fuera del rango observado
import numpy as np
# rango: 30 a 100
x = np.array([30, 40, 50, 60, 70, 80, 90, 100], dtype=float)
y = np.array([350, 360, 430, 440, 530, 540, 630, 640], dtype=float)
b1 = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean())**2).sum()
b0 = y.mean() - b1 * x.mean()      # recta del Ejemplo 9.1
print(b0 + b1 * 120)               # 738.81: valor mecanico, fuera del rango
