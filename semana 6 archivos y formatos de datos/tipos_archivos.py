# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:21:10 2025

@author: jveraz
"""

###############################
# Tipos de Archivos en Python #
###############################

##############################
# Tipos de Archivos en Python
##############################

# 📌 ¿Qué es un archivo en Python?
# Un archivo es una estructura de almacenamiento que permite guardar información
# en diferentes formatos. Los programas pueden leer, escribir y modificar estos datos.

# 📌 Principales formatos usados en Python:
# 🔹 TXT  -> Texto sin formato, útil para documentos, transcripciones y corpus literarios.
# 🔹 CSV  -> Datos tabulares separados por comas, usado en bases de datos y archivos históricos.
# 🔹 JSON -> Estructura basada en pares clave-valor, utilizada en APIs y bases de datos documentales.
# 🔹 XML  -> Formato jerárquico para modelar datos estructurados como catálogos y documentos digitales.

def explicar_tipo_archivo(tipo):
    """
    Explica el uso de diferentes tipos de archivos en Python.
    """
    explicaciones = {
        "TXT": "TXT almacena texto plano y es útil para transcripciones y corpus literarios.",
        "CSV": "CSV almacena información tabular y se usa en bases de datos y registros históricos.",
        "JSON": "JSON estructura datos en pares clave-valor, ideal para APIs y almacenamiento flexible.",
        "XML": "XML organiza datos en una estructura jerárquica, utilizada en documentos digitales complejos."
    }
    return explicaciones.get(tipo.upper(), "Tipo de archivo desconocido.")

# 🔹 Ejemplo de uso:
print(explicar_tipo_archivo("TXT"))
print(explicar_tipo_archivo("CSV"))
print(explicar_tipo_archivo("JSON"))
print(explicar_tipo_archivo("XML"))

