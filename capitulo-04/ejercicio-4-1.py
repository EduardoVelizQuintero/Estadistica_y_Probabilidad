# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 4: Variables aleatorias continuas y sus distribuciones de probabilidad
# Ejercicio 4.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 4.1 - Densidad f(x) = 3x^2 en (0, 1)
# La proporcion vendida antes del mediodia

# quad integra una funcion entre dos limites
from scipy.integrate import quad

# Se define la densidad como una funcion de x
def f(x):
    return 3 * x**2

# Control obligatorio: el area total debe ser 1
print(quad(f, 0, 1)[0])           # 1.0

# La acumulada es F(x) = x^3: se escribe a mano
def F_acum(x):
    return x**3

# Probabilidad de vender menos de la mitad
print(F_acum(0.5))                # 0.125

# La misma probabilidad, integrando la densidad
print(quad(f, 0, 0.5)[0])         # 0.125

# Probabilidad entre 0.5 y 0.8: resta de acumuladas
print(F_acum(0.8) - F_acum(0.5))  # 0.387

# Esperanza: integral de x por f(x)
print(quad(lambda x: x * f(x), 0, 1)[0])       # 0.75

# Segundo momento: integral de x^2 por f(x)
ex2 = quad(lambda x: x**2 * f(x), 0, 1)[0]
print(ex2)                        # 0.6

# Varianza por la forma de calculo y desviacion
var_x = ex2 - 0.75**2
print(var_x)                      # 0.0375
print(var_x**0.5)                 # 0.193649...
