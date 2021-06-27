#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 13: Elabore pseudocódigo para el caso en que se desean escribir los números del 1 al 100.

class Contar:
    def Variables(self):
        print("Contar los números del 1 al 100 usando While")
        i=1
        while i <=100:
            print(i)
            i=i+1
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 
        
contar= Contar()
contar.Variables()