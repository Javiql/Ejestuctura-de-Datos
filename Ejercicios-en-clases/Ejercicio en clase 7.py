#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1
#Fecha:21/06/2021

class Cargo:
    secuencia=0
    def __init__(self,des="Sin cargo"):
        Cargo.secuencia=Cargo.secuencia+1
        self.codigo=Cargo.secuencia 
        self.descripcion=des
if __name__ == "__main__":
    cargo1=Cargo ()
    print("Cargo1:",cargo1.codigo,cargo1.descripcion)

    cargo2=Cargo("Docente")
    print("Cargo2:",cargo2.codigo,cargo2.descripcion)

    cargo3 = Cargo()
    print("Cargo3:",cargo3.codigo,cargo3.descripcion)
    print(Cargo.secuencia)