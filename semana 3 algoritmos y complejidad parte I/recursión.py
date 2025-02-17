# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:20:16 2025

@author: jveraz
"""

#############
# Recursión #
#############

# 🔹 ¿Qué es la recursión?
# Es una técnica en la que una función se llama a sí misma para resolver un problema en partes más pequeñas.
# Es útil cuando un problema puede descomponerse en versiones más pequeñas de sí mismo.

# 🔹 Aplicación en Humanidades:
# - Encontrar patrones en un texto usando funciones recursivas.
# - Generar árboles genealógicos de personajes históricos o literarios.

def factorial(n):
    """
    Calcula el factorial de un número usando recursión.
    """
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))
