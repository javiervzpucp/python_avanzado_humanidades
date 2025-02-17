# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:31:40 2025

@author: jveraz
"""

###################################################
# Ordenamiento Avanzado (Quick Sort y Merge Sort) #
###################################################

# 🔹 Quick Sort
# Un algoritmo de ordenamiento eficiente basado en particiones.

def quick_sort(lista):
    """
    Implementación de Quick Sort.
    Divide y ordena de forma recursiva los elementos menores y mayores a un pivote.
    """
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivote]
    medio = [x for x in lista if x == pivote]
    derecha = [x for x in lista if x > pivote]
    return quick_sort(izquierda) + medio + quick_sort(derecha)

# 🔹 Merge Sort
# Divide la lista en mitades y luego las combina ordenadamente.

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izquierda = merge_sort(lista[:medio])
    derecha = merge_sort(lista[medio:])
    return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    resultado = []
    i = j = 0
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado
