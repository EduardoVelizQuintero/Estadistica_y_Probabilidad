# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 11: Diseno de experimentos
# Ejercicio 11.1 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 11.1 - sorteo del orden dentro de cada minimercado (bloque)
import numpy as np
# semilla: sorteo reproducible y auditable
rng = np.random.default_rng(2026)
minimercados = [f"M{i}" for i in range(1, 7)]  # los seis bloques
orden = rng.choice(["nuevo-primero", "actual-primero"], size=6)
# plan de asignacion, un orden por bloque
for m, o in zip(minimercados, orden):
    print(m, o)
