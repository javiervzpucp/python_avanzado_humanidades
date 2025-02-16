# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:38:34 2025

@author: jveraz
"""

#############
# Funciones #
#############

# 🔹 ¿Qué es una función?
# Una función es una regla matemática que asocia cada entrada con UNA única salida.
# Se representa como f(x) = y, donde x es la entrada y y la salida.
# En Humanidades, podemos usar funciones para modelar datos culturales, frecuencia de palabras, 
# número de referencias a un autor en un corpus, etc.

# 🔹 Características de una función:
# - **Inyectiva (uno a uno)**: No hay dos entradas con la misma salida.
# - **Sobreyectiva**: Cada posible salida tiene al menos una entrada que la produce.
# - **Biyectiva**: Es inyectiva y sobreyectiva al mismo tiempo.

# 🔹 Ejemplo: Cantidad de referencias a un autor en un corpus de textos.
def referencias_autor(num_textos):
    return num_textos * 3  # Supongamos que cada texto cita 3 veces al autor.

num_textos = [1, 2, 3, 4, 5]
referencias = [referencias_autor(n) for n in num_textos]

print("Referencias a un autor según el número de textos:", referencias)

# 🔹 Función lineal simple: f(x) = 2x + 1
def funcion_lineal(x):
    return 2*x + 1

valores = [1, 2, 3, 4, 5]
resultados = [funcion_lineal(x) for x in valores]

print("Valores:", valores)
print("Resultados de la función:", resultados)
