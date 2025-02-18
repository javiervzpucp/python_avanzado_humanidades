# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:43:26 2025

@author: jveraz
"""

##############
# Ejercicios #
##############

##############################
# 1️⃣ Teoría de Conjuntos
##############################

# 📝 Ejercicio 1: Definición de Conjuntos
# - Crea dos conjuntos: 
#   1. Un conjunto con los nombres de cinco autores del siglo XX.
#   2. Un conjunto con los nombres de cinco autores que escribieron novelas.
# - Muestra ambos conjuntos en pantalla.

# 📝 Ejercicio 2: Operaciones con Conjuntos
# - Usa los conjuntos del Ejercicio 1 y realiza:
#   - Unión de ambos conjuntos.
#   - Intersección entre ambos conjuntos.
#   - Diferencia entre los dos conjuntos.
#   - Comprueba si un conjunto es subconjunto del otro.

# 📝 Ejercicio 3: Aplicación de Conjuntos en Humanidades
# - Crea un conjunto de palabras frecuentes en un poema y otro de palabras frecuentes en un ensayo.
# - Encuentra:
#   - Palabras comunes a ambos textos.
#   - Palabras que solo aparecen en el poema.
#   - Palabras únicas al ensayo.

##############################
# 2️⃣ Relaciones y Funciones
##############################

# 📝 Ejercicio 4: Modelado de Relaciones
# - Crea un diccionario donde las claves sean autores y los valores sean sus obras más conocidas.
# - Muestra el diccionario.

# 📝 Ejercicio 5: Funciones Matemáticas en Humanidades
# - Crea una función `obtener_pais(autor)` que devuelva el país de origen de un autor.
# - Usa un diccionario para relacionar autores con sus países.

# 📝 Ejercicio 6: Relaciones en Datos Bibliográficos
# - Crea un diccionario que relacione obras literarias con su año de publicación.
# - Luego, escribe una función que reciba un año y devuelva las obras publicadas en ese año.

##############################
# 3️⃣ Cardinalidad y Equivalencia
##############################

# 📝 Ejercicio 7: Cardinalidad de Conjuntos
# - Crea un conjunto con 10 títulos de libros y otro con los 10 autores de esos libros.
# - Muestra la cardinalidad de cada conjunto.
# - Determina si tienen la misma cantidad de elementos.

# 📝 Ejercicio 8: Comparación de Corpus
# - Crea dos conjuntos:
#   - `corpus_literario_moderno`: con cinco títulos de novelas modernas.
#   - `corpus_literario_clasico`: con cinco títulos de novelas clásicas.
# - Compara ambos conjuntos:
#   - ¿Tienen la misma cardinalidad?
#   - ¿Comparten títulos en común?

##############################
# 4️⃣ Álgebra Booleana
##############################

# 📝 Ejercicio 9: Filtros con Condiciones Booleanas
# - Dado el siguiente conjunto de autores, filtra solo aquellos del siglo XX.
autores = [
    {"nombre": "Cervantes", "siglo": 16, "genero": "Novela"},
    {"nombre": "Shakespeare", "siglo": 16, "genero": "Teatro"},
    {"nombre": "García Márquez", "siglo": 20, "genero": "Realismo mágico"},
    {"nombre": "Borges", "siglo": 20, "genero": "Cuento"}
]

# - Filtra los autores que NO escribieron teatro.

# 📝 Ejercicio 10: Consultas de Datos
# - Dado el siguiente diccionario de autores y géneros literarios:
autores_generos = {
    "Cervantes": "Novela",
    "Shakespeare": "Teatro",
    "García Márquez": "Realismo mágico",
    "Borges": "Cuento",
    "Pizarnik": "Poesía"
}

# - Filtra los autores que escribieron novelas o realismo mágico.

##############################
# Proyecto Final - Semana 1
##############################

# 📝 Proyecto Final
# - Modela un corpus literario como conjuntos y relaciones.
# - Aplica álgebra booleana para realizar búsquedas optimizadas.
# - Representa los datos de manera visual en un gráfico (opcional).
