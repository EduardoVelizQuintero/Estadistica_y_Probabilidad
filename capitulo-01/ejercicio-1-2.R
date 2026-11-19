# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 1: Que es estadistica?
# Ejercicio 1.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 1.2 en R: media contra mediana, en tres lineas
comisiones <- c(320, 340, 350, 360, 370, 380, 390, 400, 850)
mean(comisiones)    # media con el atipico: 417.78
median(comisiones)  # mediana: 370, no se entera del 850
