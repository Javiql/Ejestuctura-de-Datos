#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 18: Calcular el factorial de N números enteros leídos de teclado.
#El problema consistirá en realizar una estructura de N iteraciones aplicando 
# el factorial de un número.

class Factorial:
    def Calcular(self):
        n=int(input("Ingresa un numero: "))
        acu=1
        for num in range(n,1,-1):
            acu =acu*num
        print("El número ingresado es:  {}  , y su factorial es:  {} ".format(n,acu))
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 

factorial= Factorial()
factorial.Calcular()