#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 6: Dado el sueldo de un empleado, encontrar el nuevo sueldo si obtiene 
#un aumento del 10% si su sueldo es inferior a $600, en caso contrario no tendrá aumento.

class Aumento:
    def Dinero(self):
        SUELDO=float(input("Ingrese el sueldo del empleado:"))
        if SUELDO < 600:
            NS=SUELDO + SUELDO*0.1
        else:
            NS=SUELDO    
        print("Sueldo a recibir:",NS)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")

aumento= Aumento()
aumento.Dinero()