# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:52:05 2025

@author: jveraz
"""

#########################
# Inversa de una matriz #
#########################

import numpy as np

# 🔹 ¿Qué es la inversa de una matriz?
# Es una matriz que, cuando se multiplica por la original, da la matriz identidad.
# Se usa en resolución de sistemas de ecuaciones y transformaciones de datos.

# 🔹 Ejemplo:
A = np.array([[2, 1], [5, 3]])

# 🔹 Determinante
determinante = np.linalg.det(A)
print("Determinante de la matriz A:", determinante)

# 🔹 Si el determinante no es 0, la matriz tiene inversa
if determinante != 0:
    A_inv = np.linalg.inv(A)
    print("Matriz inversa A⁻¹:\n", A_inv)

    # 🔹 Verificamos que A * A⁻¹ da la matriz identidad
    identidad = np.matmul(A, A_inv)
    print("Matriz identidad obtenida:\n", identidad)
else:
    print("La matriz no tiene inversa porque su determinante es 0.")
