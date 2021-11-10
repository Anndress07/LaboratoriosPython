#! /usr/bin/python3
# Marvin Andres Castro
# Este programa se encarga de calcular el FIbonacci de un numero N.
# el programa igualmente da la opcion de imprimir el tiempo que tomo en
# ejecutarse, y tambien los fibonacci de los numeros anteriores a N.
import time


class Test4:

    # aqui declaro los argumentos/variables de -c y -t. Los puse en el
    # constructor para que toda la clase tenga acceso a ellos
    def __init__(self):
        self.inicio = time.time()
        from argparse import ArgumentParser
        parser = ArgumentParser()
        parser.add_argument("numero", type=int, help="numero a calcular")
        parser.add_argument(
            "-t", "--tiempo",
            action="store_true",
            help="medir tiempo"
                            )

        parser.add_argument(
            "-c", "--completa",
            action="store_true",
        help="imprimir todos los"
            " fibonacci"
                            )

        self.args = parser.parse_args()

# calculo del fibonacci. El parametro viene de args.numero, definido
# en el metodo constructor
    def fibonacci(self, numero):

        if numero == 0:
            return 1
        if numero == 1:
            return 1
        else:
            return self.fibonacci(numero-1) + self.fibonacci(numero-2)

    def controlador(self):
        numero = self.args.numero
        if numero < 0:
            raise ValueError("Por favor ingrese un numero entero positivo")
        else:

            # calculo del tiempo empleado
            res = self.fibonacci(numero)
            parar = time.time()
            tiempo = parar - self.inicio

            # aqui no me salio como yo queria, tuve que hacer unas maniobras
            # con el if
            print("El Fibonacci del indice " + str(numero) + " es " + str(res))
            if self.args.tiempo is True and self.args.completa is False:
                print("Tiempo total de ejecucion: ")
                print(str(tiempo) + " segundos.")

            elif self.args.completa is True and self.args.tiempo is False:
                print("Serie de Fibonacci hasta el indice " + str(numero))
                for n in range(0, numero+1):
                    print(self.fibonacci(n))

            # por algun motivo el codigo anterior no puede imprimir el tiempo
            # y fibonacci completo, entonces tengo que hacer esto,
            # nada eficiente
            if self.args.tiempo is True and self.args.completa is True:
                print("Tiempo total de ejecucion: ")
                print(str(tiempo) + " segundos.")

                print("Serie de Fibonacci hasta el indice " + str(numero))
                for n in range(0, numero+1):
                    print(self.fibonacci(n))


a = Test4()
a.controlador()
