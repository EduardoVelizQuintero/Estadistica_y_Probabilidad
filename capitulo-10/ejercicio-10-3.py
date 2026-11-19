# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 10: Analisis de varianza
# Ejercicio 10.3 (Python)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 10.3 - ANOVA como regresion con indicadoras
import statsmodels.formula.api as smf
import pandas as pd
datos = pd.DataFrame({
    "ventas": [210, 230, 225, 215, 240, 255, 250, 245, 195, 205, 200, 210],
    "sucursal": ["Centro"] * 4 + ["Norte"] * 4 + ["Sur"] * 4})
ajuste = smf.ols("ventas ~ C(sucursal)", data=datos).fit()
print(ajuste.rsquared, ajuste.fvalue)  # 0.892 ; 37.05 : el mismo ANOVA
