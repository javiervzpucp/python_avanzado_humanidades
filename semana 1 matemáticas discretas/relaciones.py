# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:38:06 2025

@author: jveraz
"""

##############
# Relaciones #
##############

# 🔹 ¿Qué es una relación?
# En matemáticas, una relación es un conjunto de pares ordenados que indican una conexión entre elementos de dos conjuntos.
# En Humanidades, podemos representar relaciones de influencia, citas entre autores, relaciones temáticas en literatura, etc.

# 🔹 Ejemplo: Relación entre autores y sus movimientos literarios.
autores_movimientos = {
    "Cervantes": "Renacimiento",
    "Góngora": "Barroco",
    "Borges": "Boom Latinoamericano",
    "Cortázar": "Boom Latinoamericano",
    "Pizarnik": "Poesía Contemporánea"
}

# 🔹 Propiedades de una relación:
# - **Reflexiva**: Si cada elemento está relacionado consigo mismo.
# - **Simétrica**: Si (a, b) está en la relación, entonces (b, a) también lo está.
# - **Transitiva**: Si (a, b) y (b, c) están en la relación, entonces (a, c) también lo está.

# 🔹 Relación reflexiva: Un autor siempre pertenece a su movimiento literario.
relacion_reflexiva = {(a, a) for a in autores_movimientos.keys()}

# 🔹 Relación simétrica: Si un autor menciona a otro en su obra, el otro lo menciona también.
relacion_simetrica = {("Cervantes", "Lope de Vega"), ("Lope de Vega", "Cervantes")}

# 🔹 Relación transitiva: Si Cervantes influenció a Borges y Borges a García Márquez, entonces Cervantes influenció a García Márquez.
relacion_transitiva = {("Cervantes", "Borges"), ("Borges", "García Márquez"), ("Cervantes", "García Márquez")}

print("Relación reflexiva:", relacion_reflexiva)
print("Relación simétrica:", relacion_simetrica)
print("Relación transitiva:", relacion_transitiva)
