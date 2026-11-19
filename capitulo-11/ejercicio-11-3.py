# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.3 - plan reparado: sorteo por jornada en cada agencia
import numpy as np
rng = np.random.default_rng(2026)            # sorteo auditable
for agencia in ["centro", "norte"]:          # la agencia actua como bloque
    for jornada in range(1, 11):             # diez jornadas por agencia
        guion = rng.choice(["nuevo", "actual"])  # sorteo dentro del bloque
        print(agencia, jornada, guion)       # las replicas son las jornadas
