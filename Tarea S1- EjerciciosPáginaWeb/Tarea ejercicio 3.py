#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 3: Un vendedor recibe un sueldo base más un 10% extra por comisión de sus ventas. 
# El vendedor desea saber cuánto dinero obtendrá por concepto de comisiones por las tres 
# ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo 
# base y sus comisiones.

class Dinero:
    def Calcular(self):
        SB=float(input("Ingrese salario base:"))
        V1=float(input("Ingrese valor de venta 1:"))
        V2=float(input("Ingrese valor de venta 2:"))
        V3=float(input("Ingrese valor de venta 3:"))
        TV=V1+V2+V3
        C=TV*0.1
        TR=SB+C
        print("Su Total a Recibir es: $",TR)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")
dinero= Dinero()
dinero.Calcular()