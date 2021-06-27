#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 17: Aplicar los pasos de la metodología para la solución de un problema
# para leer un número entero N y calcular el resultado de la siguiente serie:
#1 – 1/2+ 1/3 – 1/4 +.... +/- 1/N. Resolveremos el problema utilizando bucle Repeat 
#controlado por contador y usando banderas.

class Problema:
    def Calcular(self): 
        serie= 0
        l=1
        n=int(input("Ingresa un número para la serie: "))
        band= "T"
        while l>n:
            if band ="T":
                serie=serie+(1/l)
                band="F":
            else:
                serie=serie-(1/l)
                band="T":
            l=l+1
        print(serie,band)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 
        
problema= Problema()
problema.Calcular()