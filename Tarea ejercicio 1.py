#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

# Ejercicio 1: En ejemplos anteriores, diseñamos un pseudocódigo para encontrar la superficie de un
#círculo para un radio cualquiera. El Flujograma que representa a dicho ejemplo es el siguiente:

class Área:
    def Calcular(self):
        pi=3.1416
        R =int(input("Ingrese el radio del circulo: "))
        cal =R*R
        S=cal*pi
        print("La superficie del circulo es: ",S)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")

área= Área()
área.Calcular()


