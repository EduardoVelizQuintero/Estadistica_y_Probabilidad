# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 8: Propiedades de los estimadores puntuales y metodos de estimacion
# Ejercicio 8.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 8.1 - Eficiencia relativa (Python)
sigma = 12                      # desviacion poblacional
var_a = sigma**2                # 144: una sola observacion
var_b = sigma**2 / 2            # 72: media de 2
var_c = sigma**2 / 3            # 48: media de 3

# Eficiencias respecto de A
print(var_a / var_b)            # 2.0
print(var_a / var_c)            # 3.0

# Desviaciones en dolares
print([v**0.5 for v in (var_a, var_b, var_c)])
# [12.0, 8.485..., 6.928...]
