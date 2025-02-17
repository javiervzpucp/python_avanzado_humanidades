# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:28:32 2025

@author: jveraz
"""

##############################
# Optimización de Algoritmos #
##############################

# 🔹 ¿Qué significa optimizar un algoritmo?
# Optimizar un algoritmo implica mejorar su rendimiento reduciendo la cantidad de operaciones 
# necesarias para resolver un problema.

# 🔹 Estrategias de optimización:
# 1️⃣ **Evitar cálculos repetitivos** → Guardar valores intermedios en variables o estructuras de datos.
# 2️⃣ **Usar estructuras eficientes** → Diccionarios en vez de listas para búsquedas rápidas.
# 3️⃣ **Reducir operaciones innecesarias dentro de bucles** → Usar funciones matemáticas en lugar de iteraciones.

# 🔹 Ejemplo 1: Uso de una fórmula en lugar de un bucle (mejora de O(n) a O(1))

def suma_bucle(n):
    """
    Calcula la suma de los primeros n números usando un bucle.
    Complejidad O(n) porque hay n iteraciones.
    """
    suma = 0
    for i in range(1, n+1):
        suma += i
    return suma

def suma_formula(n):
    """
    Calcula la suma de los primeros n números usando la fórmula matemática.
    Complejidad O(1) porque la fórmula se ejecuta en tiempo constante.
    """
    return n * (n + 1) // 2

print("Suma con bucle:", suma_bucle(1000))
print("Suma con fórmula:", suma_formula(1000))  # Mucho más eficiente


