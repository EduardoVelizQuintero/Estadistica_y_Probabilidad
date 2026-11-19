# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 1: Que es estadistica?
# Ejercicio 1.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 1.1 - Descripcion de 10 dias de ventas (R)
# Cada linea se comenta para poder leer el codigo como texto.

ventas <- c(82, 95, 88, 102, 95, 110,  # guarda las 10 ventas en un vector
            76, 95, 99, 108)          # en dolares por dia
n <- length(ventas)              # n = 10: el tamano de la muestra
media <- mean(ventas)            # media: suma / n, da 95
mediana <- median(ventas)        # mediana: valor central ordenado, da 95
tabla <- table(ventas)  # tabla: cuenta cuantas veces sale cada valor
moda <- as.numeric(names(tabla)[which.max(tabla)])
# la linea anterior busca el valor con mayor cuenta: la moda, 95
# R base no trae funcion de moda: se construye desde la tabla
rango <- max(ventas) - min(ventas)   # rango: 110 - 76 = 34
s <- sd(ventas)  # desviacion muestral: divide entre n-1, da 10.74
cuartiles <- quantile(ventas, probs = c(0.25, 0.75))
# cuartiles por interpolacion lineal: Q1 = 89.75 y Q3 = 101.25
riq <- IQR(ventas)               # rango intercuartilico: Q3 - Q1 = 11.50
cat("Media:", media, " Mediana:", mediana, " Moda:", moda, "\n")
cat("Rango:", rango, " s:", round(s, 2), " RIQ:", riq, "\n")
