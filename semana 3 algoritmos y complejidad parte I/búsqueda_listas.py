# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:17:17 2025

@author: jveraz
"""

######################
# Búsqueda en listas #
######################

# 🔹 ¿Qué es la búsqueda en listas?
# Es el proceso de encontrar un elemento dentro de una lista de datos.
# Se usa en Humanidades para:
# - Buscar una palabra clave en un documento.
# - Encontrar la referencia de un autor en una bibliografía.
# - Recuperar datos en bases de datos históricas o literarias.

# 🔹 Tipos de búsqueda en listas:
# - **Búsqueda lineal (O(n))**: Recorre la lista uno por uno hasta encontrar el elemento.
# - **Búsqueda binaria (O(log n))**: Solo funciona en listas ordenadas y divide la lista en partes para encontrar el elemento más rápido.

# 🔹 Explicación paso a paso de la búsqueda lineal:
# 1️⃣ Empezamos desde el primer elemento.
# 2️⃣ Comparamos con el elemento buscado.
# 3️⃣ Si coincide, devolvemos la posición.
# 4️⃣ Si no, seguimos buscando hasta el final de la lista.
# 5️⃣ Si no lo encontramos, devolvemos -1.

def busqueda_lineal(lista, objetivo):
    """
    Realiza una búsqueda lineal en la lista.
    Retorna la posición del elemento si se encuentra, o -1 si no está en la lista.
    """
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i  
    return -1  

# 🔹 Ejemplo: Buscar una palabra en una lista de términos académicos
palabras = ["autor", "historia", "lenguaje", "texto", "cultura"]
resultado = busqueda_lineal(palabras, "texto")
if resultado != -1:
    print("La palabra 'texto' está en la posición:", resultado)
else:
    print("La palabra 'texto' no se encuentra en la lista.")

