# Estadistica Matematica con Datos de Ecuador
# Eduardo Jose Veliz Quintero
# Capitulo 9: Modelos lineales y minimos cuadrados
# Ejercicio 9.3 (R)
# Codigo del libro. Repositorio: https://github.com/EduardoVelizQuintero/Estadistica_y_Probabilidad

# Ejercicio 9.3 - prediccion fuera del rango observado
x <- c(30, 40, 50, 60, 70, 80, 90, 100)   # superficies observadas
y <- c(350, 360, 430, 440, 530, 540, 630, 640)  # arriendos en dolares
ajuste <- lm(y ~ x)                        # recta del Ejemplo 9.1
predict(ajuste, newdata = data.frame(x = 120),
# 738.81 con intervalo ancho: extrapolacion
        interval = "prediction", level = 0.95)
