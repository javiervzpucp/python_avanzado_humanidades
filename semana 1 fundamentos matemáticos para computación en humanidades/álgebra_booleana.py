# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 00:42:58 2025

@author: jveraz
"""

##########################################
# Álgebra Booleana y Consultas Textuales #
##########################################

autores = [
    {"nombre": "Cervantes", "siglo": 16, "genero": "Novela"},
    {"nombre": "Shakespeare", "siglo": 16, "genero": "Teatro"},
    {"nombre": "García Márquez", "siglo": 20, "genero": "Realismo mágico"},
    {"nombre": "Borges", "siglo": 20, "genero": "Cuento"}
]

autores_siglo_20 = [a for a in autores if a["siglo"] == 20]
print("\n📌 Autores del siglo XX:", [a["nombre"] for a in autores_siglo_20])

autores_no_teatro = [a for a in autores if a["genero"] != "Teatro"]
print("\n📌 Autores que no escribieron teatro:", [a["nombre"] for a in autores_no_teatro])
