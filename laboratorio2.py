#!/usr/bin/python3
#Marvin Andres Castro

class Laboratorio2:

    def procesadorTexto(self):
        """ 
        pide el nombre completo, verifica si el string es un 
        nombre con 3 elementos. Si es un string con más de 
        3 elementos, convierte la primera letra en mayúscula 
        y las demás en minúscula. Después las concatena 
        en un string
        
        """
        parar = False
        listanombres = []
        string = ""
        import re
        special_char = re.compile('[1234567890@_!#$%^&*()<>?/\|}{~:]')
        while parar == False:
            nombre = input("Ingrese el nombre completo a digitar ")
            nombresDivididos = nombre.split(" ")
            if nombre != "SALIR" and len(nombresDivididos) < 3:
                print("ERROR: Debe digitar nombres de 3 o 4 componentes") 
            
            # verificar si tiene carácteres especiales o numeros
            # (lo busqué en internet, creo que no lo entiendo del todo bien)
            elif(special_char.search(nombre) == ( None)):
                listanombres.append(nombre)
        
            else:
                
                print("ERROR: Debe digitar nombres sin carácteres especiales o números")
            
            if nombre == "SALIR":
                parar = True
                for nombre in listanombres:
                    nombre = nombre.title()
                    if nombre != "Salir" :
                        string += nombre 
                    string += "\n"
                print(string)
                
a = Laboratorio2()  
a.procesadorTexto()
