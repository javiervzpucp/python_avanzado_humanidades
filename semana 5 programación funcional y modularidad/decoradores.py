# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 22:47:56 2025

@author: jveraz
"""

#########################
# Decoradores en Python #
#########################

# 🔹 ¿Qué son los decoradores?
# Son funciones que modifican el comportamiento de otras funciones.

# 🔹 Ejemplo: Registrar el tiempo de ejecución de una función.

import time

def medir_tiempo(funcion):
    """
    Decorador que mide el tiempo de ejecución de una función.
    """
    def envoltura(*args, **kwargs):
        inicio = time.time()
        resultado = funcion(*args, **kwargs)
        fin = time.time()
        print(f"Tiempo de ejecución: {fin - inicio:.4f} segundos")
        return resultado
    return envoltura

@medir_tiempo
def tarea_pesada():
    time.sleep(2)
    print("Tarea completada.")

tarea_pesada()

