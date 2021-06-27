#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 12:Calcular la suma de los cuadrados de los primeros 100 enteros y escribir el resultado.

class Suma:
    def Calcular(self):
        i=1
        suma=0
        x=range(100)
        for i in x:
            suma=suma+i*i
            print("Suma: ",suma) 
        print("\n")
        print("**FIN DE LA EJECUCIÓN**") 

suma= Suma()
suma.Calcular()