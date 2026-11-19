# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.2 - efectos de un factorial 2 x 2
celdas <- matrix(c(38, 44, 47, 61), nrow = 2, byrow = TRUE,
                 dimnames = list(riego = c("secano", "riego"),
                                 fert = c("estandar", "reforzado")))
mean(celdas["riego", ]) - mean(celdas["secano", ])   # efecto riego: +13
# efecto fert.: +10
mean(celdas[, "reforzado"]) - mean(celdas[, "estandar"])
# interaccion: +8
(celdas[2, 2] - celdas[2, 1]) - (celdas[1, 2] - celdas[1, 1])
