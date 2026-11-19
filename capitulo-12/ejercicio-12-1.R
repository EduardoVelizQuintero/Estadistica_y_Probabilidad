# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.1 - chi cuadrado en una tabla 2 x 2
tabla <- matrix(c(40, 20, 30, 30), nrow = 2, byrow = TRUE,
                dimnames = list(genero = c("mujeres", "hombres"),
                                compra = c("si", "no")))
chisq.test(tabla, correct = FALSE)  # chi2 = 3.43 ; gl = 1 ; p = 0.064
