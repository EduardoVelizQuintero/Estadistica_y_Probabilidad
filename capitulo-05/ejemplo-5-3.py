# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 5: Distribuciones muestrales y teorema central del limite
# Ejemplo guia 5.3: simulacion del TLC (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejemplo 5.3 (guia) - Simulacion del TLC (Python)
import numpy as np
rng = np.random.default_rng(2026)  # semilla reproducible

# 4000 muestras de n = 30, cada una resumida por su media
muestras = rng.exponential(scale=400, size=(4000, 30))
medias30 = muestras.mean(axis=1)   # una media por fila
print(medias30.mean())             # cerca de 397.34
print(medias30.std(ddof=1))        # cerca de 72.91
print(400 / 30**0.5)               # teoria: 73.03
