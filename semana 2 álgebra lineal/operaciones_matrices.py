# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:51:41 2025

@author: jveraz
"""

############################
# Operaciones con matrices #
############################

import numpy as np

# 🔹 ¿Por qué son útiles las operaciones con matrices?
# En el análisis de datos en Humanidades, muchas veces necesitamos combinar información 
# o transformar datos en formatos distintos. 

# 🔹 Suma de matrices (Combinar datos)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

suma_matrices = A + B
print("Suma de matrices:\n", suma_matrices)

# 🔹 Producto matricial (Multiplicación de matrices)
# Se usa para modelar relaciones entre elementos o transformar datos.
producto_matricial = np.matmul(A, B)
print("Producto matricial:\n", producto_matricial)

# 🔹 Determinante de una matriz (Nos indica si una matriz es invertible)
determinante = np.linalg.det(A)
print("Determinante de la matriz A:", determinante)
