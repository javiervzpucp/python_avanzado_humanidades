# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:42:33 2025

@author: jveraz
"""

##########################
# Relaciones y Funciones #
##########################

relacion_autor_obra = {
    "Cervantes": "Don Quijote",
    "Shakespeare": "Hamlet",
    "García Márquez": "Cien años de soledad",
    "Borges": "Ficciones"
}

print("\n📌 Relación entre autores y obras:")
for autor, obra in relacion_autor_obra.items():
    print(f"{autor} → {obra}")

def obtener_pais(autor):
    paises = {
        "Cervantes": "España",
        "Shakespeare": "Inglaterra",
        "García Márquez": "Colombia",
        "Borges": "Argentina"
    }
    return paises.get(autor, "Desconocido")

print("\n📌 País de Borges:", obtener_pais("Borges"))
