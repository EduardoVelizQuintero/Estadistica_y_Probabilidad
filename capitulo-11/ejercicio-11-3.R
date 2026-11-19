# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.3 - plan reparado: sorteo por jornada en cada agencia
set.seed(2026)                               # sorteo auditable
jornadas <- expand.grid(agencia = c("centro", "norte"), jornada = 1:10)
jornadas$guion <- ifelse(runif(nrow(jornadas)) < 0.5, "nuevo", "actual")
head(jornadas)  # 20 jornadas: esas son las replicas
