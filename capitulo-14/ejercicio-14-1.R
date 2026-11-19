# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.1 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.1 - beta-binomial con a priori uniforme
# A priori Beta(1, 1) ; datos: 3 exitos en 10 clientes
a_post <- 1 + 3          # alfa a posteriori: 4
b_post <- 1 + (10 - 3)   # beta a posteriori: 8
a_post / (a_post + b_post)                    # media a posteriori: 0.33
qbeta(c(0.025, 0.975), a_post, b_post)  # intervalo creible 95%: 0.11 a 0.61
