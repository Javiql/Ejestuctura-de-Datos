#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 8: Leer tres números enteros diferentes entre sí y determinar el número mayor de los tres.

class Numeros:
    def NumeroMayor(self):
        n1= int(input("Ingrese el primer número entero: "))
        n2= int(input("Ingrese el segundo número entero: "))
        n3= int(input("Ingrese el tercer número entero: "))
        if n1>n2 and n1>n3:
            NM=n1
        else:
            if n2>n3:
                NM=n2
            else:
                NM=n3
        print("El número mayor es:",NM)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
numeros = Numeros()
numeros.NumeroMayor()