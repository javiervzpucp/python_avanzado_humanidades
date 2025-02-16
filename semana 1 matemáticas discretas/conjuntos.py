# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:37:13 2025

@author: jveraz
"""

##############
# Conjuntos  #
##############

# 🔹 ¿Qué es un conjunto?
# Un conjunto es una colección de elementos únicos, sin un orden específico.
# En Humanidades, los conjuntos pueden representar agrupaciones de autores, géneros literarios,
# palabras en un texto, entre otros.

# 🔹 Propiedades de los conjuntos:
# - Son **no ordenados**: No hay una posición específica para cada elemento.
# - No hay **elementos repetidos**: Si se intenta agregar un elemento repetido, el conjunto lo ignora.
# - Se pueden realizar **operaciones matemáticas** sobre ellos.

# 🔹 Ejemplo 1: Definir conjuntos con géneros literarios
generos_poesia = {"lírica", "épica", "dramática"}
generos_narrativa = {"novela", "cuento", "épica"}

# 🔹 Operaciones con conjuntos
# Unión: Todos los géneros mencionados en cualquiera de los dos conjuntos.
union_generos = generos_poesia | generos_narrativa

# Intersección: Géneros que están en ambos conjuntos.
interseccion_generos = generos_poesia & generos_narrativa

# Diferencia: Géneros exclusivos de la poesía.
diferencia_generos = generos_poesia - generos_narrativa

print("Unión de géneros:", union_generos)
print("Intersección de géneros:", interseccion_generos)
print("Diferencia (géneros exclusivos de la poesía):", diferencia_generos)

# 🔹 Conjunto Potencia (Power Set): Todos los subconjuntos posibles de un conjunto.
from itertools import chain, combinations

def conjunto_potencia(S):
    return list(chain.from_iterable(combinations(S, r) for r in range(len(S) + 1)))

print("Conjunto potencia de géneros de poesía:", conjunto_potencia(generos_poesia))
