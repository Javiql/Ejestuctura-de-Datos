#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 10: Un ejemplo en el cual usamos el operador lógico AND sería:
#Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de 
# ellos obtiene dos calificaciones denotadas como C1 y C2. El aspirante que 
# obtenga calificaciones mayores que 80 en ambos exámenes es aceptado; en 
# caso contrario es rechazado.

class Calificaciones:
    def Notas(self):
        C1= float(input("Ingrese la primera Calificacion: "))
        C2= float(input("Ingrese la segunda Calificacion: "))
        if C1>=80 and C2>= 80:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Ha sido --->ACEPTADO")
        else:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Ha sido ---> RECHAZADO")
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
        
calificaciones = Calificaciones()
calificaciones.Notas()