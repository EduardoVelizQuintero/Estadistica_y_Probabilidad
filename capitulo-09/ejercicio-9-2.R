# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.2 - contraste para la correlacion
r <- 0.75                          # correlacion muestral
n <- 10                            # tamano de muestra
t <- r * sqrt(n - 2) / sqrt(1 - r^2)  # estadistico t: 3.21
2 * pt(-abs(t), df = n - 2)        # valor p bilateral: 0.0125
