#!/usr/bin/python3

class Labo1:

        def labo1(self):
            parar = False
            while parar == False:
                    
                letra = input("Ingrese el caracter que desea repetir ")
                
                        
                datoValido = False
                while datoValido == False:
                  try:
                    repetir = int(input("Ingrese el numero de caracteres pora la base de la piramide "))
                    if repetir > 0:
                      datoValido = True
                    
                    else: 
                      print("Por favor ingrese valores positivos o mayores a 0")
                  except:
                    print("Por favor ingrese un dato valido")
        
                n = 0
                while n != repetir:
                    print(letra * (repetir-n))
                    n = n + 1
                    
                salir = input("digite x si desea salir: ")
                if salir == "x":
                    parar = True

a = Labo1()
a.labo1()
