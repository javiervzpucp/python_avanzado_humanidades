# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:22:16 2025

@author: jveraz
"""

#################################
# Manejo de Archivos CSV y JSON #
#################################

import csv
import json

# 🔹 Crear y leer archivos CSV y JSON con datos estructurados.

# 🔹 Crear un archivo CSV con datos estructurados
def crear_csv(nombre_archivo):
    """
    Crea un archivo CSV con datos de autores y obras literarias.
    """
    with open(nombre_archivo, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Autor", "Año", "Obra"])
        escritor.writerow(["Cervantes", 1605, "Don Quijote"])
        escritor.writerow(["Shakespeare", 1603, "Hamlet"])
        escritor.writerow(["Gabriel García Márquez", 1967, "Cien años de soledad"])

crear_csv("autores.csv")

# 🔹 Convertir un archivo CSV a JSON
def csv_a_json(archivo_csv, archivo_json):
    """
    Convierte un archivo CSV en JSON.
    """
    with open(archivo_csv, "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        datos = list(lector)

    with open(archivo_json, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)

csv_a_json("autores.csv", "autores.json")

