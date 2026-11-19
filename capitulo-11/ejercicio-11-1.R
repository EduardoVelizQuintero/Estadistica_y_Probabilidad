# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.1 - sorteo del orden dentro de cada minimercado (bloque)
set.seed(2026)  # semilla: sorteo reproducible y auditable
minimercados <- paste0("M", 1:6)            # los seis bloques
orden <- sample(c("nuevo-primero", "actual-primero"), 6, replace = TRUE)
data.frame(minimercado = minimercados, orden = orden)  # plan de asignacion
