#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 9: Diseñar un algoritmo tal que dados como datos dos variables
# de tipo entero, obtenga el resultado de la siguiente función:

class Algoritmo:
    def Datos(self):
        NUM= int(input("Ingresa la primera variable: "))
        V= int(input("Ingresa la segunda Variable: "))
        if NUM== 1:
            Resp=100*V
        elif NUM==2:
            Resp=pow(100,V)
        elif NUM==3:
            Resp=100/V
        else:
            Resp=0   
        print("Respuesta:",Resp)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
algoritmo = Algoritmo()
algoritmo.Datos()