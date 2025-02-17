# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:20:45 2025

@author: jveraz
"""

######################
# Serie de Fibonacci #
######################

# 🔹 ¿Qué es la serie de Fibonacci?
# Es una secuencia en la que cada número es la suma de los dos anteriores.
# Se usa en modelado matemático, crecimiento poblacional y análisis de patrones.

# 🔹 Aplicación en Humanidades:
# - Algunas estructuras narrativas en literatura pueden seguir patrones similares a la serie de Fibonacci.
# - Se usa en estudios sobre proporciones en el arte y arquitectura.

def fibonacci(n):
    """
    Calcula el término n de la serie de Fibonacci usando recursión.
    """
    if n <= 0:
        return "Número inválido"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci de 6:", fibonacci(6))
