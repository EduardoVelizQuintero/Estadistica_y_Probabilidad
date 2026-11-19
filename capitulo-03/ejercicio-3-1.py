# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 3: Variables aleatorias discretas y sus distribuciones de probabilidad
# Ejercicio 3.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 3.1 - Esperanza y varianza de las entregas
# Tabla del enunciado: conteos y sus probabilidades

# Los valores posibles de X: entregas por hora
x = [0, 1, 2, 3]

# La funcion de probabilidad p(x), en el mismo orden
p = [0.20, 0.40, 0.30, 0.10]

# Control obligatorio: las probabilidades suman 1
print(sum(p))                     # 1.0

# Esperanza: suma de x por p(x), termino a termino
# zip recorre las dos listas a la par
mu = sum(xi * pi for xi, pi in zip(x, p))
print(mu)                         # 1.3

# Segundo momento: suma de x^2 por p(x)
ex2 = sum(xi**2 * pi for xi, pi in zip(x, p))
print(ex2)                        # 2.5

# Varianza por la forma de calculo: E(X^2) - mu^2
var_x = ex2 - mu**2
print(var_x)                      # 0.81
print(var_x**0.5)                 # 0.9

# El ingreso es g(X) = 3X: se aplica sobre la misma tabla
ingreso = [3 * xi for xi in x]
print(sum(g * pi for g, pi in zip(ingreso, p)))  # 3.9
print(3 * var_x**0.5)             # 2.7 dolares de desviacion
