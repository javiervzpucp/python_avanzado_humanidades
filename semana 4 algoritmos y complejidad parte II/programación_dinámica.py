# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:29:04 2025

@author: jveraz
"""

#######################################
# Programación Dinámica y Memoización #
#######################################

# 🔹 ¿Qué es la programación dinámica?
# Es una técnica de optimización que evita realizar cálculos repetidos, almacenando
# resultados intermedios y reutilizándolos.

# 🔹 ¿Qué es memoización?
# La memoización es una técnica que almacena los valores de funciones ya calculadas en una estructura de datos.

# 🔹 Fibonacci con y sin memoización

def fibonacci_recursivo(n):
    """
    Calcula la serie de Fibonacci de manera ineficiente.
    Complejidad O(2^n), porque recalcula muchos valores repetidos.
    """
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

def fibonacci_memo(n, memoria={}):
    """
    Calcula Fibonacci usando memoización.
    Almacena los valores ya calculados para evitar recomputaciones.
    Complejidad O(n), mucho más eficiente que la versión recursiva sin memoización.
    """
    if n in memoria:
        return memoria[n]
    if n <= 1:
        return n
    memoria[n] = fibonacci_memo(n - 1, memoria) + fibonacci_memo(n - 2, memoria)
    return memoria[n]

print("Fibonacci normal de 35:", fibonacci_recursivo(35))  # Tardará mucho
print("Fibonacci optimizado de 35:", fibonacci_memo(35))  # Mucho más rápido

