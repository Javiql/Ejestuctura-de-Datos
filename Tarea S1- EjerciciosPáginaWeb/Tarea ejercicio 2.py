#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

#Ejercicio 2:En una tienda se ofrece un descuento del 15% sobre el total de la compra 
# y un cliente desea saber cuánto deberá pagar finalmente por su compra.

class Descuento:
    def Calcular(self):
        TC=float(input("Ingrese total de la compra:"))
        D=TC*0.15
        CP=TC-D
        print()
        print("Valor a pagar: $",CP)
        print("\n")
        print("**FIN DE LA EJECUCIÓN**")

descuento= Descuento()
descuento.Calcular()

