# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 13: Estadistica no parametrica
# Ejercicio 13.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 13.3 - las tres decisiones en codigo
from scipy import stats
# (a) n grande: stats.ttest_ind(grupo1, grupo2, equal_var=False)
# (b) n pequeno con extremo: stats.mannwhitneyu(tiempos_A, tiempos_B)
# (c) ordinal, tres grupos: stats.kruskal(sucursal_1, sucursal_2,
#     sucursal_3)
# Nota: en el libro, la continuacion de la linea anterior perdio el signo #
# al imprimirse; aqui se restituye para que el archivo ejecute. El contenido
# es el mismo del libro.
