"""
    @reroes
    Manejo de estructuras
"""

#Mi nombre es:Edgar y mi apelldio es: Guamo 

diccionario = {"nombre": "Edgar", "apellido": "Guamo"}
diccionario2 = {"nombre": "Zacarias", "apellido": "ElCapo"}
lista  = [diccionario, diccionario2]

print("Imprimir diccionario")
for l in lista:
    midiccionario = l 
    print("Mi nombre es: %s y mi apelldio es: %s" % \
         (midiccionario["nombre"], midiccionario["apellido"]))


