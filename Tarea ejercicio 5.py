#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 5:  Dado como dato la calificación de un alumno en un examen, escriba “aprobado” 
# si su calificación es mayor o igual que 7 y “Reprobado” en caso contrario.

class Nota:
    def Calificacion(self):
        cal=float(input("Ingrese la calificacion obtenida:"))
        if cal >= 7 :
            print("APROBADO")
        else:
            print("REPROBADO")
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")

nota = Nota()
nota.Calificacion()