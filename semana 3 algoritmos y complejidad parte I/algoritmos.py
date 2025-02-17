# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:04:49 2025

@author: jveraz
"""

##############
# Algoritmos #
##############

# 🔹 ¿Qué es un algoritmo?
# Un algoritmo es una secuencia de pasos organizados para resolver un problema.
# Se pueden encontrar algoritmos en la vida cotidiana:
# - Seguir una receta de cocina.
# - Organizar libros en una biblioteca.
# - Cruzar la calle con un semáforo.

# 🔹 En programación, un algoritmo es una serie de instrucciones que una computadora ejecuta
# para transformar una entrada en una salida.

# 📌 Estructura de un algoritmo:
# 1️⃣ Entrada: Recibe datos.
# 2️⃣ Proceso: Realiza operaciones con los datos.
# 3️⃣ Salida: Devuelve un resultado.

# 🔹 Ejemplo en programación: Contar palabras en un texto.
def contar_palabras(texto):
    """
    Recibe un texto y devuelve el número total de palabras que contiene.
    """
    palabras = texto.split()  # Separa el texto en palabras
    return len(palabras)  # Devuelve la cantidad de palabras

texto = "La inteligencia artificial está transformando las humanidades."
print("Número de palabras:", contar_palabras(texto))
