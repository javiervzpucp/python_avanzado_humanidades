# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 23:23:03 2025

@author: jveraz
"""

##############
# Ejercicios #
##############

# 🔹 Cada ejercicio debe ser resuelto con código Python.
# 🔹 Se recomienda leer las explicaciones antes de resolver los ejercicios.

##############################
# 1️⃣ Archivos de Texto (.txt)
##############################

# 📝 Ejercicio 1: Crear y leer un archivo de texto
# - Crea un archivo llamado "poema.txt" y escribe al menos 5 versos de un poema.
# - Luego, ábrelo y muestra su contenido en la consola.

# 📝 Ejercicio 2: Contar palabras en un archivo de texto
# - Escribe una función que lea "poema.txt" y cuente cuántas veces aparece una palabra dada.

# 📝 Ejercicio 3: Extraer líneas con una palabra clave
# - Escribe una función que busque todas las líneas en "poema.txt" que contengan la palabra "amor".

##############################
# 2️⃣ Archivos CSV
##############################

# 📝 Ejercicio 4: Crear un archivo CSV con datos históricos
# - Crea un archivo CSV "historia.csv" que contenga los siguientes datos:
#   | Año | Evento                         | Lugar  |
#   |----|--------------------------------|--------|
#   | 1492 | Descubrimiento de América    | América |
#   | 1789 | Revolución Francesa          | Francia |
#   | 1969 | Llegada a la Luna            | EE.UU.  |

# - Luego, escribe una función que lea "historia.csv" y muestre el contenido en la consola.

# 📝 Ejercicio 5: Filtrar información de un CSV
# - Escribe una función que lea "historia.csv" y devuelva solo los eventos ocurridos en el siglo XX.

##############################
# 3️⃣ Archivos JSON
##############################

# 📝 Ejercicio 6: Crear y leer un archivo JSON con datos de autores
# - Crea un archivo JSON "autores.json" con la siguiente estructura:
#   [
#      {"nombre": "Cervantes", "obra": "Don Quijote", "año": 1605},
#      {"nombre": "Shakespeare", "obra": "Hamlet", "año": 1603},
#      {"nombre": "Gabriel García Márquez", "obra": "Cien años de soledad", "año": 1967}
#   ]
# - Luego, escribe una función que lea "autores.json" y muestre los datos en la consola.

# 📝 Ejercicio 7: Filtrar datos en JSON
# - Escribe una función que lea "autores.json" y devuelva solo las obras publicadas después del año 1800.

# 📝 Ejercicio 8: Modificar datos en JSON
# - Escribe una función que agregue un nuevo autor y su obra a "autores.json".

##############################
# 4️⃣ Archivos XML
##############################

# 📝 Ejercicio 9: Crear y leer un archivo XML con datos de libros
# - Crea un archivo XML "biblioteca.xml" con al menos 3 libros y sus autores.
# - Luego, escribe una función que lea el XML y extraiga solo los títulos de los libros.

# 📝 Ejercicio 10: Buscar un libro en XML
# - Escribe una función que reciba un autor como parámetro y devuelva las obras que ha escrito en "biblioteca.xml".

# 📝 Ejercicio 11: Convertir datos de JSON a XML
# - Escribe una función que convierta los datos de "autores.json" a "biblioteca.xml".

##############################
# 5️⃣ Conversión entre formatos
##############################

# 📝 Ejercicio 12: Convertir CSV a JSON
# - Escribe una función que convierta "historia.csv" en un archivo JSON "historia.json".

# 📝 Ejercicio 13: Convertir JSON a CSV
# - Escribe una función que convierta "autores.json" en un archivo CSV "autores.csv".

# 📝 Ejercicio 14: Convertir JSON a XML
# - Escribe una función que convierta "autores.json" en un archivo XML "autores.xml".

##############################
# 6️⃣ Ejercicios Desafío
##############################

# 📝 Ejercicio 15: Analizar un corpus de texto
# - Descarga un texto literario en formato TXT (puedes usar "poema.txt").
# - Escribe una función que cuente cuántas palabras diferentes hay en el texto.

# 📝 Ejercicio 16: Extraer nombres propios de un texto
# - Escribe una función que lea "poema.txt" y extraiga los nombres propios presentes en el texto.

# 📝 Ejercicio 17: Validar estructura de un XML
# - Escribe una función que verifique si "biblioteca.xml" tiene la estructura esperada.

# 📝 Ejercicio 18: Crear un conversor de formatos
# - Escribe un programa que permita al usuario convertir un archivo de un formato a otro.
# - Debe aceptar los formatos TXT, CSV, JSON y XML.

##############################
# Ejercicio Final - Proyecto Pequeño
##############################

# 📝 Ejercicio 19: Construir un catálogo de libros en diferentes formatos
# - Escribe un programa que permita al usuario agregar, modificar y eliminar libros en una base de datos de libros.
# - Los datos deben poder almacenarse y recuperarse en CSV, JSON y XML.
# - Agrega opciones para buscar libros por título o autor.
