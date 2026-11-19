# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 12: Datos categoricos
# Ejercicio 12.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 12.3 - esperados pequenos: prueba exacta de Fisher
tabla <- matrix(c(8, 2, 4, 6), nrow = 2, byrow = TRUE,
                dimnames = list(tratamiento = c("nuevo", "habitual"),
                                mejoria = c("si", "no")))
# esperados: 6, 4 ; 6, 4 (dos bajo 5)
chisq.test(tabla, correct = FALSE)$expected
fisher.test(tabla)  # prueba exacta para la tabla 2 x 2
