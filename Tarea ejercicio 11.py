#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 11:Una escuela aplica dos exámenes a sus aspirantes, por lo que cada uno de ellos 
# obtiene dos calificaciones denotadas como C1 y C2. El aspirante que obtenga una calificación 
# mayor que 90 en cualquiera de los exámenes es aceptado; en caso contrario es rechazado.

class Calificaciones:
    def Notas(self):
        C1= float(input("Ingrese la primera Calificacion: "))
        C2= float(input("Ingrese la segunda Calificacion: "))
        if C1>=90 and C2>=90:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Ha sido --->ACEPTADO")
        else:
            print(("Sus notas son: {} , {} ").format(C1,C2))
            print("Ha sido ---> RECHAZADO")
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
        
calificaciones = Calificaciones()
calificaciones.Notas()