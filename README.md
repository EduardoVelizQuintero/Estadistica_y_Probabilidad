# Estadística Matemática con Datos de Ecuador

Código en R y Python de los ejercicios resueltos del libro
**«Estadística Matemática con Datos de Ecuador»**, de Eduardo José Véliz
Quintero (primera edición, noviembre de 2026).

El libro tiene 16 capítulos, 48 ejercicios resueltos y 192 ejercicios
propuestos con sus respuestas al final del libro. Este repositorio contiene el
código de los ejercicios resueltos que lo llevan en el libro: **72 scripts**
(37 en R y 35 en Python), correspondientes a 36 de los 48 ejercicios resueltos
y al ejemplo guía de simulación del teorema central del límite (Ejemplo 5.3).

Los 12 ejercicios resueltos restantes no tienen código en el libro (son de
redacción, de concepto o de cálculo a mano) y por eso no tienen archivo aquí:
1.3, 2.2, 2.3, 3.2, 3.3, 4.2, 4.3, 6.3, 7.2, 8.2, 15.2 y 15.3. Los ejercicios
7.3 y 8.3 solo tienen versión en R en el libro (son simulaciones). Ningún
ejercicio propuesto lleva código en su respuesta, así que no hay archivos de
los 192 propuestos. El código se ofrece con fines didácticos, sin garantía de
ningún tipo, como indica la página de derechos del libro.

## Estructura

```text
capitulo-01/   ¿Qué es estadística?
capitulo-02/   Probabilidad
capitulo-03/   Variables aleatorias discretas y sus distribuciones de probabilidad
capitulo-04/   Variables aleatorias continuas y sus distribuciones de probabilidad
capitulo-05/   Distribuciones muestrales y teorema central del límite
capitulo-06/   Estimación
capitulo-07/   Prueba de hipótesis
capitulo-08/   Propiedades de los estimadores puntuales y métodos de estimación
capitulo-09/   Modelos lineales y mínimos cuadrados
capitulo-10/   Análisis de varianza
capitulo-11/   Diseño de experimentos
capitulo-12/   Datos categóricos
capitulo-13/   Estadística no paramétrica
capitulo-14/   Métodos de Bayes
capitulo-15/   Distribuciones multivariantes
capitulo-16/   Funciones de variables aleatorias
```

Cada carpeta tiene un archivo por ejercicio resuelto y por lenguaje, por
ejemplo `capitulo-01/ejercicio-1-1.R` y `capitulo-01/ejercicio-1-1.py`. Los
comentarios están sin tildes, como en el libro, para que el código corra en
cualquier parte. Cada archivo indica en su encabezado el capítulo y el
ejercicio del libro al que corresponde.

## Requisitos

- **Python 3.12.3** (o superior) con numpy, scipy y pandas. El paquete
  `statsmodels` solo lo necesitan `capitulo-10/ejercicio-10-2.py` y
  `capitulo-10/ejercicio-10-3.py`. Instalación con pip (ver
  `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```
- **R 4.3.3** (o superior). El código usa solo R base: ningún script pide
  paquetes adicionales.

## Cómo ejecutar

Desde la carpeta del capítulo que quieras, por ejemplo:

```bash
cd capitulo-01
python3 ejercicio-1-1.py
Rscript ejercicio-1-1.R
```

Los valores que el código debe imprimir están comentados en cada archivo y
explicados en el libro, en la solución de cada ejercicio.

## Verificación

Todos los scripts se ejecutaron el 19 de noviembre de 2026 y terminaron sin
errores: **Python 35/35 y R 37/37** (ver `VERIFICACION.md`, con la tabla
completa, los avisos esperados y la única corrección aplicada). En esa
verificación se usó Python 3.12.3 (numpy 1.26.4, scipy 1.11.4, pandas 2.1.4,
statsmodels 0.15.0) y R 4.3.3 con R base.

## Cómo subir este contenido a GitHub

El repositorio https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad
ya existe y está vacío. Para subir estos archivos, desde una terminal con git
instalado:

```bash
git clone https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad.git
cd Estadistica_y_Probabilidad
# Copia aquí todo el contenido de esta carpeta (capitulo-01 … capitulo-16,
# README.md, requirements.txt, VERIFICACION.md)
git add .
git commit -m "Codigo en R y Python de los ejercicios resueltos"
git push origin main
```

También se puede subir por la web de GitHub: abre el repositorio, pulsa
*Add file → Upload files* y arrastra el contenido de esta carpeta.
