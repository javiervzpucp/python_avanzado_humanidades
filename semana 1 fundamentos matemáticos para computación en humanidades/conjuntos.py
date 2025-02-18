# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:42:00 2025

@author: jveraz
"""

###################################
# Conjuntos y Operaciones Básicas #
###################################

autores_siglo_20 = {"Borges", "García Márquez", "Pizarnik", "Cortázar", "Vallejo"}
autores_boom = {"García Márquez", "Cortázar", "Fuentes", "Vargas Llosa"}

print("\n📌 Autores del siglo XX:", autores_siglo_20)
print("📌 Autores del Boom Latinoamericano:", autores_boom)

union = autores_siglo_20 | autores_boom
interseccion = autores_siglo_20 & autores_boom
diferencia = autores_siglo_20 - autores_boom

print("\n📌 Todos los autores considerados:", union)
print("📌 Autores en ambos grupos:", interseccion)
print("📌 Autores del siglo XX que no pertenecen al Boom:", diferencia)
