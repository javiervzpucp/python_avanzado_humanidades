# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:19:51 2025

@author: jveraz
"""

################
# Ordenamiento #
################

# 🔹 ¿Qué es el ordenamiento de listas?
# Es un proceso para organizar elementos en un orden determinado, ya sea de menor a mayor (ascendente)
# o de mayor a menor (descendente). Se usa en múltiples áreas, incluyendo Humanidades Digitales.

# 🔹 Aplicaciones en Humanidades:
# - Ordenar libros por fecha de publicación.
# - Organizar palabras por frecuencia en un corpus de textos.
# - Clasificar autores según el número de referencias en bibliografías académicas.

# 🔹 Existen varios algoritmos de ordenamiento:
# 1️⃣ **Ordenamiento Burbuja** (O(n²)): Simple pero ineficiente para grandes listas.
# 2️⃣ **Ordenamiento por Inserción** (O(n²)): Funciona bien para listas pequeñas o casi ordenadas.
# 3️⃣ **Ordenamiento Rápido (Quicksort)** (O(n log n)): Muy eficiente en la mayoría de los casos.
# 4️⃣ **Ordenamiento con sort() de Python** (Timsort - O(n log n)): Método optimizado por defecto en Python.

# ===================================================
# 1️⃣ Ordenamiento Burbuja
# ===================================================
def burbuja(lista):
    n = len(lista)
    for i in range(n - 1):
        intercambio = False  
        for j in range(n - 1 - i):  
            if lista[j] > lista[j + 1]:  
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  
                intercambio = True
        if not intercambio:
            break  

# ===================================================
# 2️⃣ Ordenamiento por Inserción
# ===================================================
def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and clave < lista[j]:  
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave  

# ===================================================
# 3️⃣ Ordenamiento Rápido (Quicksort)
# ===================================================
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]  
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]  
    mayores = [x for x in lista if x > pivote]  
    return quicksort(menores) + iguales + quicksort(mayores)

# ===================================================
# 4️⃣ Ordenamiento con sort() de Python
# ===================================================
def ordenamiento_python(lista):
    lista.sort()  

# 🔹 Aplicación práctica en Humanidades:
# Supongamos que tenemos una lista de años de publicación de libros.
años_publicacion = [1998, 2005, 1983, 2015, 2021, 1990]

burbuja(años_publicacion.copy())
print("Ordenamiento Burbuja:", años_publicacion)

insercion(años_publicacion.copy())
print("Ordenamiento por Inserción:", años_publicacion)

print("Ordenamiento Quicksort:", quicksort(años_publicacion.copy()))

ordenamiento_python(años_publicacion.copy())
print("Ordenamiento con sort():", años_publicacion)
