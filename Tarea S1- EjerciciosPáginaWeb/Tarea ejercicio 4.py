#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 4:  Construir un algoritmo tal, que dado como dato la calificación
#de un alumno en un examen.

class Nota:
    def Calificacion(self):
        cal=float(input("Ingrese la calificacion obtenida:"))
        if cal >= 7 :
            print("APROBADO")
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
nota= Nota()
nota.Calificacion()