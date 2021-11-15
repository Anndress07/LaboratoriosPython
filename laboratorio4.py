#!/usr/bin/python3
# Marvin Andres Castro Castro

import numpy as np


class Matriz():
    """
    Método constructor donde se establecen los objetos de filas y columnas
    que se usarán para toda la clase
    """

    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz2 = ""

    """
    Método que genera matrices nulas, dadas la cantidad de filas y
    columnas
    """
    def constructor_matrices(self):
        matriz = np.zeros((self.filas, self.columnas), dtype=np.int32)
        return matriz

    """
    Método especial que imprime la matriz como un string
    """
    def __str__(self):
        return str(self.constructor_matrices()).replace("[","").replace("]","")

    """
    Método que se encarga de imprimir el valor en el índice dado
        ifila = en qué fila se encuentra el valor deseado (contando desde 0)
        icolumna = en qué columna se encuentra el valor deseado (Desde 0 )
    """
    def get(self, ifila, icolumna):
       try:
           return self.constructor_matrices()[ifila, icolumna]
       except:
           return "Error: El índice que ingresó no se encuentra en la matriz"

    """
    Método que se encarga de sustituir un valor en una posición específica
        sfila = en qué fila se encuentra el valor a sustituir (desde 0)
        scolumna = en qué columna se encuentra el valor a sustituir (desde 0)
        sustit = el valor por el que se va a sustituir
    """
    def set(self, sfila, scolumna, sustit):
        # if sfila > self.filas:
        #     print("El indice de fila dado es mayor al de la matriz")
        # elif scolumna > self.columnas:
        #     print("El indice de columna dado es mayor al de la matriz")
        try:
            self.matriz2 =np.zeros((self.filas, self.columnas), dtype=np.int32)
            self.matriz2[sfila, scolumna] = sustit
            return self.matriz2
        except:
            return "Error: El índice que ingresó no se encuentra en la matriz"

    """
    Método que permite sumar la matriz1 y matriz2
    """
    def __add__(self, other):
        # return self.constructor_matrices() + other.constructor_matrices()
        if self.matriz2.shape == other.matriz2.shape:
            return self.matriz2 + other.matriz2
        else:
            print("Error: Las matrices deben tener dimensiones equivalentes")
    """
    Método que permite restar la matriz1 y matriz2
    """
    def __sub__(self, other):
        if self.matriz2.shape == other.matriz2.shape:
            return self.matriz2 - other.matriz2
        else:
            print("Error: Las matrices deben tener dimensiones equivalentes")


# =============================================================================
# Demostración del programa con una matriz 3x3 y una 3x6
# =============================================================================
matriz1 = Matriz(3, 3)
matriz2 = Matriz(3, 6)
print("La matriz 1 es \n")
print("", matriz1, "\n")
print("La matriz 2 es \n")
print("", matriz2)
# demostracion del metodo get, para obtener el valor de la fila 2, columna 3
print("\nEl valor ubicado en la fila 2 y columna 3 es igual a " + "\n" +
      str(matriz1.get(2-1, 3-1)))
print("")
# demostracion del metodo set,
print("Añadiendo el valor 5 en la fila 2, columna 4 de la matriz 1... ")
print(str(matriz1.set(1, 3, 5)) + "\n")
print("Añadiendo el valor 10 en la fila 3, columna 6 en la matriz 2...")
print(matriz2.set(2, 5, 10))

print("Sumando matriz1 + matriz2...")
matriz3 = matriz1 + matriz2
print("\n")

print("Restando matriz1 - matriz2...")
matriz4 = matriz1 - matriz2
print("\n")
# =============================================================================
# demostracion para matrices cuadradas
# =============================================================================
print("Digite 'siguiente' para ver los resultados de dos matrices 4x4.")
print("Digite cualquier otro cáracter para salir.")
condicional = input("")
if condicional == "siguiente":
    matriz1 = Matriz(4, 4)
    matriz2 = Matriz(4, 4)
    print("La matriz 1 es \n")
    print("", matriz1, "\n")
    print("La matriz 2 es \n")
    print("", matriz2)
    # demostracion del metodo get
    print("\nEl valor ubicado en la fila 2 y columna 3 es igual a " + "\n" +
          str(matriz1.get(2-1, 3-1)))
    print("")
    # demostracion del metodo set,
    print("Añadiendo el valor 15 en la fila 4, columna 4 de la matriz 1... ")
    print(str(matriz1.set(4-1, 4-1, 15)) + "\n")
    print("Añadiendo el valor 25 en la fila 3, columna 3 en la matriz 2...")
    print(matriz2.set(3-1, 3-1, 25))

    print("Sumando matriz1 + matriz2...")
    matriz3 = matriz1 + matriz2
    print(matriz3)
    print("\n")

    print("Restando matriz1 - matriz2...")
    matriz4 = matriz1 - matriz2
    print(matriz4)
    print("\n")

else:
    print("")
