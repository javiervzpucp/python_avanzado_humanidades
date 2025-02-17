# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 19:05:20 2025

@author: jveraz
"""

###############################
# Complejidad de un algoritmo #
###############################

import time

# 🔹 ¿Qué es la notación O (O-grande)?
# Es una manera de describir cómo crece el tiempo o la memoria usada por un algoritmo a medida que aumentan los datos de entrada.
# No mide el tiempo exacto de ejecución, sino cómo **escala** el algoritmo con más datos.

# 🔹 Importancia en Humanidades Digitales:
# - Si analizamos una gran cantidad de textos, elegir el algoritmo correcto puede hacer la diferencia entre un análisis rápido o uno que nunca termine.
# - Un mal algoritmo puede tardar días en procesar una biblioteca digital grande.

# 🔹 Tipos comunes de O-grande:
# - **O(1) → Tiempo constante:** El algoritmo siempre tarda lo mismo, sin importar el tamaño de los datos.
# - **O(log n) → Tiempo logarítmico:** Crece lentamente a medida que aumentan los datos. Ejemplo: búsqueda binaria.
# - **O(n) → Tiempo lineal:** Crece proporcionalmente a los datos. Ejemplo: recorrer una lista.
# - **O(n²) → Tiempo cuadrático:** El tiempo aumenta muy rápido, no es eficiente. Ejemplo: algunos algoritmos de ordenamiento.
# - **O(2ⁿ) → Tiempo exponencial:** Crece extremadamente rápido, casi siempre es ineficiente.

# 🔹 Ejemplo práctico: Contar elementos en una lista con distintas estrategias.

lista = list(range(100000))  # Lista con 100,000 elementos

# ===================================================
# 🔹 Estrategia 1: Recorrer la lista manualmente (O(n))
# ===================================================
def contar_elementos_ineficiente(lista):
    """
    Cuenta los elementos recorriendo toda la lista uno por uno.
    Complejidad: O(n) → El tiempo crece proporcionalmente con la cantidad de datos.
    """
    contador = 0
    for _ in lista:
        contador += 1
    return contador

inicio = time.time()
contar_elementos_ineficiente(lista)
fin = time.time()
print("Tiempo con O(n) (búsqueda manual):", fin - inicio, "segundos")

# ===================================================
# 🔹 Estrategia 2: Usar len() de Python (O(1))
# ===================================================
inicio = time.time()
len(lista)  # Python internamente conoce el tamaño sin recorrer la lista
fin = time.time()
print("Tiempo con O(1) (acceso directo con len()):", fin - inicio, "segundos")

# ===================================================
# 🔹 Estrategia 3: Recursión para contar elementos (O(n), pero menos eficiente)
# ===================================================
def contar_recursivo(lista):
    """
    Cuenta los elementos usando recursión.
    Complejidad: O(n), pero más ineficiente que la versión iterativa
    debido al gasto extra de memoria en llamadas recursivas.
    """
    if not lista:
        return 0
    return 1 + contar_recursivo(lista[1:])

inicio = time.time()
contar_recursivo(lista[:1000])  # Se limita a 1000 elementos por seguridad
fin = time.time()
print("Tiempo con O(n) (recursión ineficiente):", fin - inicio, "segundos")
