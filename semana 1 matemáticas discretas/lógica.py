# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:03:57 2025

@author: jveraz
"""

##################################
# Lógica Proposicional en Python #
##################################

# 🔹 ¿Qué es la lógica proposicional?
# Es un sistema que estudia el razonamiento lógico usando proposiciones y operadores lógicos.

# 🔹 Operadores lógicos en Python:
# - NOT → `not`
# - AND → `and`
# - OR  → `or`
# - Implicación lógica (p → q) → Se implementa como `not p or q`

# 🔹 Evaluación de expresiones lógicas

p = True
q = False

print("p AND q:", p and q)  # Evaluar la conjunción lógica
print("p OR q:", p or q)  # Evaluar la disyunción lógica
print("NOT p:", not p)  # Evaluar la negación lógica
print("p → q:", (not p) or q)  # Evaluar la implicación lógica

# 🔹 Tabla de verdad en Python

def tabla_verdad():
    """
    Genera una tabla de verdad para operaciones lógicas.
    """
    print(" p | q | p AND q | p OR q | NOT p | p → q ")
    print("-----------------------------------------")
    for p in [True, False]:
        for q in [True, False]:
            print(f" {int(p)} | {int(q)} |   {int(p and q)}    |   {int(p or q)}    |   {int(not p)}   |   {int((not p) or q)} ")

tabla_verdad()

# 🔹 Aplicación en Humanidades Digitales
# Supongamos que queremos analizar la relación entre autores en una base de datos.

autores = {
    "Autor A": {"Autor B": True, "Autor C": False},
    "Autor B": {"Autor A": True, "Autor C": True},
    "Autor C": {"Autor A": False, "Autor B": True},
}

# Queremos verificar si dos autores han colaborado en un artículo:
def han_colaborado(autor1, autor2, base_datos):
    """
    Determina si dos autores han colaborado juntos en una publicación.
    """
    return base_datos.get(autor1, {}).get(autor2, False)

print("¿Autor A y Autor B han trabajado juntos?", han_colaborado("Autor A", "Autor B", autores))
print("¿Autor A y Autor C han trabajado juntos?", han_colaborado("Autor A", "Autor C", autores))
