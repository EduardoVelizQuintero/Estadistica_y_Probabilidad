# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 14: Metodos de Bayes
# Ejercicio 14.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 14.3 - probabilidad a posteriori sobre el parametro
# A posteriori: mu ~ Normal(534.48, 18.57)
1 - pnorm(520, mean = 534.48, sd = 18.57)   # P(mu > 520 | datos) = 0.78
# P(500 < mu < 560) = 0.88
pnorm(560, 534.48, 18.57) - pnorm(500, 534.48, 18.57)
