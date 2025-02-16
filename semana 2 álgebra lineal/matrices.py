# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:51:17 2025

@author: jveraz
"""

############
# Matrices #
############

import numpy as np

# 🔹 ¿Qué es una matriz?
# Una matriz es una tabla de números organizada en filas y columnas.
# Se usa para representar datos estructurados y analizar relaciones complejas.

# 🔹 Aplicaciones en Humanidades:
# Las matrices se pueden usar para representar relaciones entre autores,
# co-ocurrencia de palabras en textos o análisis de redes semánticas.

# 🔹 Ejemplo: Relación entre libros y géneros literarios
# Filas: Libros
# Columnas: Géneros (Humor, Ciencia Ficción, Aventura)

matriz_libros = np.array([
    [1, 0, 1],  # "Don Quijote" tiene humor y aventura.
    [0, 1, 1],  # "1984" tiene ciencia ficción y aventura.
    [1, 0, 0]   # "La Celestina" tiene humor, pero no otros géneros.
])

print("Matriz de libros y géneros:\n", matriz_libros)

# 🔹 Transposición de una matriz (Intercambiar filas por columnas)
matriz_transpuesta = np.transpose(matriz_libros)
print("Matriz transpuesta:\n", matriz_transpuesta)
