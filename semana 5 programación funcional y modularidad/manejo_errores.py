# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:48:56 2025

@author: jveraz
"""

###############################
# Manejo de Errores en Python #
###############################

# 🔹 ¿Por qué manejar errores?
# 📌 Evita que el programa se detenga inesperadamente.

# 🔹 Ejemplo con try-except-finally
try:
    numero = int(input("Ingresa un número: "))
    print(f"El doble del número es {numero * 2}")
except ValueError:
    print("Error: Debes ingresar un número entero.")
finally:
    print("Ejecución finalizada.")

