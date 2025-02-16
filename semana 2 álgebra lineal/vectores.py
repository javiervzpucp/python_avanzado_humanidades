# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:47:09 2025

@author: jveraz
"""

############
# Vectores #
############

import numpy as np

# 🔹 ¿Qué es un vector?
# Un vector es una lista de números que representan magnitudes en varias dimensiones.
# En términos simples, un vector es una estructura matemática que nos ayuda a organizar 
# datos en una línea o en un espacio multidimensional.

# 🔹 Aplicaciones en Humanidades:
# Un vector puede representar la frecuencia de palabras en un texto,
# la popularidad de un tema en distintos periodos o las conexiones entre autores.

# 🔹 Ejemplo: Frecuencia de palabras clave en un texto
vector_texto1 = np.array([3, 5, 2])  # "Amor" aparece 3 veces, "Muerte" 5 veces, "Vida" 2 veces.
vector_texto2 = np.array([1, 4, 3])  # "Amor" 1 vez, "Muerte" 4 veces, "Vida" 3 veces.

print("Vector del Texto 1:", vector_texto1)
print("Vector del Texto 2:", vector_texto2)

# 🔹 Operaciones con vectores
# Suma de vectores (frecuencia combinada de palabras)
suma_vectores = vector_texto1 + vector_texto2

# Producto escalar entre dos vectores (medida de similitud entre textos)
producto_escalar = np.dot(vector_texto1, vector_texto2)

print("Suma de vectores:", suma_vectores)
print("Producto escalar entre los textos:", producto_escalar)

