# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejemplo guia 5.3: simulacion del TLC (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejemplo 5.3 (guia) - Simulacion del TLC (R)
set.seed(2026)                 # semilla: corrida reproducible
m <- 4000                      # numero de muestras simuladas

# Medias de 4000 muestras de n = 30 desde una exponencial
# de media 400 (la poblacion simplificada del ingreso)
medias30 <- replicate(m, mean(rexp(30, rate = 1/400)))
mean(medias30)                 # cerca de 397.34 en esta corrida
sd(medias30)                   # cerca de 72.91; teoria: 73.03
400 / sqrt(30)                 # el error estandar teorico

# Lo mismo con n = 5: la forma todavia cojea a la derecha
medias5 <- replicate(m, mean(rexp(5, rate = 1/400)))
sd(medias5)                    # cerca de 176.17; teoria: 178.89
