# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:22:42 2025

@author: jveraz
"""

#################################
# Procesamiento de Archivos XML #
#################################

import xml.etree.ElementTree as ET

# 🔹 Crear y leer archivos XML con información jerárquica.

# 🔹 Crear un archivo XML con datos de libros
def crear_xml(nombre_archivo):
    """
    Crea un archivo XML con datos de libros.
    """
    biblioteca = ET.Element("biblioteca")

    libros = [
        {"titulo": "Don Quijote", "autor": "Cervantes", "año": "1605"},
        {"titulo": "Hamlet", "autor": "Shakespeare", "año": "1603"},
        {"titulo": "Cien años de soledad", "autor": "García Márquez", "año": "1967"}
    ]

    for libro in libros:
        nodo_libro = ET.SubElement(biblioteca, "libro")
        ET.SubElement(nodo_libro, "titulo").text = libro["titulo"]
        ET.SubElement(nodo_libro, "autor").text = libro["autor"]
        ET.SubElement(nodo_libro, "año").text = libro["año"]

    arbol = ET.ElementTree(biblioteca)
    arbol.write(nombre_archivo, encoding="utf-8", xml_declaration=True)

crear_xml("biblioteca.xml")

# 🔹 Leer un archivo XML y extraer títulos de libros
def extraer_titulos_xml(nombre_archivo):
    """
    Extrae títulos de libros desde un archivo XML.
    """
    arbol = ET.parse(nombre_archivo)
    raiz = arbol.getroot()
    
    titulos = [libro.find("titulo").text for libro in raiz.findall("libro")]
    return titulos

print("Títulos en XML:", extraer_titulos_xml("biblioteca.xml"))

