#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 14: Diseñe un pseudocódigo para calcular la suma y producto de N números enteros, 
# utilizando un bucle controlado por el usuario.

class Numeros:
    def Calcular(self):
        prod=1
        suma=0
        resp=input(str("¿Desea ingresar números?  (S/N)"))
        while resp != "n" and resp!= "N":
            num=int(input("Ingresa un número: "))
            suma=suma+num
            prod=prod*num
            resp=input(str("¿Quieres continuar? (S/N)"))
        print("Total de la suma es:",suma,)
        print("Total del producto es: ",prod)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 
        
numeros= Numeros()
numeros.Calcular()