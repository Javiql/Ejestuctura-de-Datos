#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1
#Fecha:21/06/2021

class Cargo:
    def __init__(self):
        self.codigo=99 
        self.descripcion="Sin cargo"
    
cargo1= Cargo ()
print("Cargo1",cargo1.codigo,cargo1.descripcion)
cargo2=Cargo()
cargo2.codigo=1
cargo2.descripcion="Docente"
print("Cargo2",cargo2.codigo,cargo2.descripcion)
cargo3 = Cargo()
cargo3.descripcion="Conserje"
print("Cargo3",cargo3.codigo,cargo3.descripcion)