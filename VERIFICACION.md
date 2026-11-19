# Verificación del código — 19 de noviembre de 2026

Todos los scripts se ejecutaron en esta máquina y terminaron con salida 0
(sin errores). Entorno de verificación:

- **Python 3.12.3** — numpy 1.26.4, scipy 1.11.4, pandas 2.1.4, statsmodels 0.15.0
  (statsmodels solo lo usan `capitulo-10/ejercicio-10-2.py` y `ejercicio-10-3.py`;
  se instaló en un entorno virtual para la verificación; en el Python del
  sistema de esta máquina no estaba instalado).
- **R 4.3.3** (2024-02-29), instalado con `sudo apt-get install -y r-base-core`.
  El código usa solo R base: ningún script pide paquetes con `library()`.

Resultado: **Python 35/35, R 37/37**.

## Corrección aplicada (1)

- `capitulo-13/ejercicio-13-3.py`: en el libro, la continuación de la línea del
  comentario `# (c) ordinal, tres grupos: stats.kruskal(sucursal_1, sucursal_2,`
  perdió el signo `#` al imprimirse y quedó como `    sucursal_3)`, lo que
  produce `IndentationError`. En el repositorio se restituyó el `#` y se dejó
  una nota en el propio archivo. El contenido es el mismo del libro. **El libro
  impreso tiene el mismo defecto en ese bloque** y conviene corregirlo en la
  próxima revisión del interior.

## Avisos durante la ejecución (no son errores)

Son avisos propios de los ejercicios, esperados por su tema:

- `capitulo-12/ejercicio-12-3.R`: `Chi-squared approximation may be incorrect`
  (frecuencias esperadas pequeñas; por eso el ejercicio usa la prueba exacta
  de Fisher).
- `capitulo-13/ejercicio-13-1.R`, `ejercicio-13-2.R` y `ejercicio-13-2.py`:
  no se puede calcular el valor p exacto con empates o con diferencias cero
  (los ejercicios tratan justamente de empates y de una diferencia cero).

## Scripts sin salida al ejecutarse como programa

- `capitulo-02/ejercicio-2-1.py`: sus valores quedan como expresiones sueltas,
  que en Python solo se muestran en modo interactivo (REPL o Jupyter); como
  script no imprime nada, pero ejecuta sin error y los valores están en los
  comentarios. En R, las expresiones sueltas sí se imprimen.
- `capitulo-13/ejercicio-13-3.R` y `capitulo-13/ejercicio-13-3.py`: son solo
  comentarios con las llamadas que corresponden a cada caso (no hay datos en
  el ejercicio), así que no producen salida. El `.py` además importa scipy.

## Ejercicios resueltos sin código en el libro

12 de los 48 ejercicios resueltos no tienen código en el libro (son de
redacción, de concepto o de cálculo a mano) y por eso no tienen archivo aquí:
1.3, 2.2, 2.3, 3.2, 3.3, 4.2, 4.3, 6.3, 7.2, 8.2, 15.2 y 15.3. Los ejercicios
7.3 y 8.3 solo tienen versión en R en el libro (son simulaciones); no se
inventó una versión en Python. Ningún ejercicio propuesto tiene código en su
respuesta del apéndice, así que no se extrajo código de los 192 propuestos.

## Tabla completa

| Archivo | Lenguaje | Resultado | Salida |
|---|---|---|---|
| `capitulo-01/ejercicio-1-1.R` | R | OK (salida 0) | con salida |
| `capitulo-01/ejercicio-1-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-01/ejercicio-1-2.R` | R | OK (salida 0) | con salida |
| `capitulo-01/ejercicio-1-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-02/ejercicio-2-1.R` | R | OK (salida 0) | con salida |
| `capitulo-02/ejercicio-2-1.py` | Python | OK (salida 0) | sin salida |
| `capitulo-03/ejercicio-3-1.R` | R | OK (salida 0) | con salida |
| `capitulo-03/ejercicio-3-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-04/ejercicio-4-1.R` | R | OK (salida 0) | con salida |
| `capitulo-04/ejercicio-4-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-05/ejemplo-5-3.R` | R | OK (salida 0) | con salida |
| `capitulo-05/ejemplo-5-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-1.R` | R | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-2.R` | R | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-3.R` | R | OK (salida 0) | con salida |
| `capitulo-05/ejercicio-5-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-06/ejercicio-6-1.R` | R | OK (salida 0) | con salida |
| `capitulo-06/ejercicio-6-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-06/ejercicio-6-2.R` | R | OK (salida 0) | con salida |
| `capitulo-06/ejercicio-6-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-07/ejercicio-7-1.R` | R | OK (salida 0) | con salida |
| `capitulo-07/ejercicio-7-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-07/ejercicio-7-3.R` | R | OK (salida 0) | con salida |
| `capitulo-08/ejercicio-8-1.R` | R | OK (salida 0) | con salida |
| `capitulo-08/ejercicio-8-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-08/ejercicio-8-3.R` | R | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-1.R` | R | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-2.R` | R | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-3.R` | R | OK (salida 0) | con salida |
| `capitulo-09/ejercicio-9-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-1.R` | R | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-2.R` | R | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-3.R` | R | OK (salida 0) | con salida |
| `capitulo-10/ejercicio-10-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-1.R` | R | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-2.R` | R | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-3.R` | R | OK (salida 0) | con salida |
| `capitulo-11/ejercicio-11-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-12/ejercicio-12-1.R` | R | OK (salida 0) | con salida |
| `capitulo-12/ejercicio-12-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-12/ejercicio-12-2.R` | R | OK (salida 0) | con salida |
| `capitulo-12/ejercicio-12-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-12/ejercicio-12-3.R` | R | OK (salida 0) | con salida (avisos: ver notas) |
| `capitulo-12/ejercicio-12-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-13/ejercicio-13-1.R` | R | OK (salida 0) | con salida (avisos: ver notas) |
| `capitulo-13/ejercicio-13-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-13/ejercicio-13-2.R` | R | OK (salida 0) | con salida (avisos: ver notas) |
| `capitulo-13/ejercicio-13-2.py` | Python | OK (salida 0) | con salida (avisos: ver notas) |
| `capitulo-13/ejercicio-13-3.R` | R | OK (salida 0) | sin salida |
| `capitulo-13/ejercicio-13-3.py` | Python | OK (salida 0) | sin salida |
| `capitulo-14/ejercicio-14-1.R` | R | OK (salida 0) | con salida |
| `capitulo-14/ejercicio-14-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-14/ejercicio-14-2.R` | R | OK (salida 0) | con salida |
| `capitulo-14/ejercicio-14-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-14/ejercicio-14-3.R` | R | OK (salida 0) | con salida |
| `capitulo-14/ejercicio-14-3.py` | Python | OK (salida 0) | con salida |
| `capitulo-15/ejercicio-15-1.R` | R | OK (salida 0) | con salida |
| `capitulo-15/ejercicio-15-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-1.R` | R | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-1.py` | Python | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-2.R` | R | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-2.py` | Python | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-3.R` | R | OK (salida 0) | con salida |
| `capitulo-16/ejercicio-16-3.py` | Python | OK (salida 0) | con salida |
