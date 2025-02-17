# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:47:06 2025

@author: jveraz
"""

########################################
# Funciones Lambda y Map-Filter-Reduce #
########################################

# 🔹 ¿Qué son las funciones lambda?
# Son funciones anónimas que pueden escribirse en una sola línea.

# Ejemplo básico:
doble = lambda x: x * 2
print("Doble de 3:", doble(3))  # 6

##############################
# 1️⃣ Uso de map()
##############################

# 🔹 Aplica una función a todos los elementos de una lista.
palabras = ["shakespeare", "cervantes", "borges"]
palabras_mayusculas = list(map(str.upper, palabras))
print("Palabras en mayúsculas:", palabras_mayusculas)

##############################
# 2️⃣ Uso de filter()
##############################

# 🔹 Filtra elementos de una lista según una condición.
palabras_largas = list(filter(lambda palabra: len(palabra) > 8, palabras))
print("Palabras con más de 8 letras:", palabras_largas)

##############################
# 3️⃣ Uso de reduce()
##############################

# 🔹 Reduce aplica una función acumulativa.
from functools import reduce

numeros = [1, 2, 3, 4]
suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma total:", suma_total)  # 10

