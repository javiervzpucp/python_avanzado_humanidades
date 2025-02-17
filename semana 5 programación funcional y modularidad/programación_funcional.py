# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:45:58 2025

@author: jveraz
"""

####################################
# Programación Funcional en Python #
####################################

# 🔹 ¿Qué es la programación funcional?
# Es un paradigma donde las funciones son tratadas como objetos de primera clase.
# Esto significa que pueden:
# ✅ Ser pasadas como argumentos a otras funciones.
# ✅ Retornar otras funciones como resultado.
# ✅ Ser almacenadas en variables.

# 🔹 ¿Por qué es útil en Humanidades Digitales?
# 📌 Se usa en procesamiento de texto (por ejemplo, filtrado de palabras en análisis literario).
# 📌 Permite escribir código más limpio y reutilizable en proyectos de datos históricos.

##############################
# 1️⃣ Funciones Puras
##############################

# 🔹 Una función pura es aquella que NO modifica variables externas y SIEMPRE devuelve el mismo resultado.

# ❌ No es pura (modifica la variable externa)
contador = 0
def aumentar_contador():
    global contador
    contador += 1
    return contador

# ✅ Versión pura
def aumentar_contador_puro(contador):
    return contador + 1

print("Función pura:", aumentar_contador_puro(5))  # 6

##############################
# 2️⃣ Funciones de Orden Superior
##############################

# 🔹 Las funciones de orden superior pueden recibir funciones como parámetros o retornarlas.

# Ejemplo: Función que aplica una transformación a cada palabra de un texto.

def aplicar_transformacion(texto, transformacion):
    """
    Aplica una transformación a cada palabra de un texto.
    """
    palabras = texto.split()
    return " ".join(transformacion(palabra) for palabra in palabras)

# Usamos la función anterior para convertir un texto a mayúsculas.
print(aplicar_transformacion("Python es increíble", str.upper))

