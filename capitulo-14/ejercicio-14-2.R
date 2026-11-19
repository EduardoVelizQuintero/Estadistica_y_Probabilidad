# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.2 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.2 - Poisson-gamma conjugada
# A priori Gamma(forma = 8, tasa = 2) ; datos: 18 llegadas en 3 horas
forma_post <- 8 + 18        # forma a posteriori: 26
tasa_post <- 2 + 3          # tasa a posteriori: 5
forma_post / tasa_post      # media a posteriori: 5.2 por hora
qgamma(c(0.025, 0.975), shape = forma_post, rate = tasa_post)  # 3.40 a 7.38
