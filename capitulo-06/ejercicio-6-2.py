# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 6: Estimacion
# Ejercicio 6.2 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 6.2 en Python: el mismo calculo
import math  # math: raiz cuadrada y redondeo hacia arriba
p = 45 / 120                         # proporcion muestral: 0.375
margen = 1.96 * math.sqrt(p*(1-p)/120)  # margen normal al 95%: 0.0866
print(p - margen, p + margen)        # intervalo: 0.288 a 0.462
n_nec = 1.96**2 * p*(1-p) / 0.03**2  # n para margen de 0.03: aprox. 1001
print(math.ceil(n_nec))              # redondear hacia arriba: 1001
