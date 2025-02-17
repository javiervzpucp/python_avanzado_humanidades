# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:30:44 2025

@author: jveraz
"""

####################
# Búsqueda Binaria #
####################

# 🔹 ¿Cómo funciona la búsqueda binaria?
# Divide el problema en mitades en cada iteración, reduciendo drásticamente el número de comparaciones.

def busqueda_binaria(lista, objetivo):
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1  # No encontrado

numeros = [1, 3, 5, 7, 9, 11, 15]
print("Posición de 7:", busqueda_binaria(numeros, 7))
