# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:21:45 2025

@author: jveraz
"""

###############################
# Manejo de Archivos de Texto #
###############################

# 📌 Aplicaciones en Humanidades Digitales:
# 🔹 Procesamiento de corpus literarios, documentos históricos y transcripciones.

# 🔹 Crear un archivo de texto con múltiples líneas
def crear_archivo_texto(nombre_archivo):
    """
    Crea un archivo de texto con citas literarias.
    """
    citas = [
        "En un lugar de la Mancha, de cuyo nombre no quiero acordarme...",
        "Ser o no ser, esa es la cuestión.",
        "Muchos años después, frente al pelotón de fusilamiento...",
        "El amor en los tiempos del cólera es una historia de paciencia."
    ]
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("\n".join(citas))

crear_archivo_texto("citas_literarias.txt")

# 🔹 Leer archivo línea por línea y contar palabras
def contar_palabras(nombre_archivo):
    """
    Lee un archivo de texto y cuenta la frecuencia de palabras.
    """
    from collections import Counter
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower()
    palabras = texto.split()
    frecuencia = Counter(palabras)
    return frecuencia

print("Frecuencia de palabras:", contar_palabras("citas_literarias.txt"))

