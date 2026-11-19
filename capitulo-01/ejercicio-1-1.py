# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 1: Que es estadistica?
# Ejercicio 1.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 1.1 - Descripcion de 10 dias de ventas (Python)
# El mismo procedimiento de R, paso a paso, en otro lenguaje.

import numpy as np            # numpy: calculo numerico con vectores
from statistics import mode   # mode: la moda estadistica de una lista

ventas = np.array([82, 95, 88, 102, 95, 110,  # las 10 ventas, en dolares
                   76, 95, 99, 108])          # como arreglo numerico
n = len(ventas)               # n = 10: tamano de la muestra
media = ventas.mean()         # media: suma / n, da 95.0
mediana = np.median(ventas)   # mediana: valor central ordenado, da 95.0
moda = mode(ventas.tolist())  # moda: el valor mas frecuente, 95
rango = ventas.max() - ventas.min()  # rango: 110 - 76 = 34
s = ventas.std(ddof=1)        # desviacion muestral: ddof=1 divide entre n-1
q1, q3 = np.percentile(ventas, [25, 75])  # cuartiles, interpolacion lineal
riq = q3 - q1  # rango intercuartilico: 101.25 - 89.75 = 11.50
print(f"Media: {media:.2f}  Mediana: {mediana:.2f}  Moda: {moda}")
print(f"Rango: {rango}  s: {s:.2f}  Q1: {q1:.2f}")
print(f"Q3: {q3:.2f}  RIQ: {riq:.2f}")
