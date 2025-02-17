# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:30:02 2025

@author: jveraz
"""

####################################
# Análisis de Complejidad Avanzado #
####################################

# 🔹 ¿Cómo evaluar la eficiencia de un algoritmo?
# La notación Big-O permite describir la cantidad de operaciones que un algoritmo
# necesita en función de la entrada.

# 🔹 Ejemplo: Comparación de diferentes complejidades

import time

def suma_cuadrados_n(n):  # Complejidad O(n)
    """
    Calcula la suma de los cuadrados de los primeros n números usando un solo bucle.
    """
    total = 0
    for i in range(n):
        total += i**2
    return total

def suma_cuadrados_n2(n):  # Complejidad O(n^2)
    """
    Calcula la suma de los cuadrados usando dos bucles anidados.
    Ineficiente en comparación con O(n).
    """
    total = 0
    for i in range(n):
        for j in range(n):
            total += i*j
    return total

n = 1000
inicio = time.time()
suma_cuadrados_n(n)
print("Tiempo O(n):", time.time() - inicio)

inicio = time.time()
suma_cuadrados_n2(n)
print("Tiempo O(n^2):", time.time() - inicio)  # Mucho más lento

