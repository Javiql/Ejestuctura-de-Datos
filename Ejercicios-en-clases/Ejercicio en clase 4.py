#Nombre: Javier Santiago Quiroz Lastre
#Aula: Software A1

class sintaxis:
    instancia=0
     #__init__ Metodo constructor que se ejecuta cuando se instancia la clase cuyo objetivo es crear
     #e iniciar los atributos de la clase. self es un objetivo que representa la clase creada
    def __init__(self ,dato="llamando al constructor1"):
        self.frase=dato #atributo de instancia
        sintaxis.instancia = sintaxis.instancia+1
    
    def usoVariables(self):
        edad, _peso=23, 64.5
        nombres = 'Javier Quiroz'
        Tipo_sexo = 'M'
        civil = True
        # tuplas = () son colecciones de datos de cualquier tipo inmutables
        usuario=()
        usuario=('jquirozl','1234','jquirozl@gmail.com')
        # print(usuario[2],nombres[7])
        # #usuario[3] = "Naranjito"
        # #lista = [] colecciones mutables
        materias=[]
        materias=['Programación Web','PHP','POO']
        aux=materias[1]
        materias[1]="python"
        materias.append("Go")
        #print(materias,aux, materias[1])
        
        #diccionario = {} colecciones de objetos clave:valor tipo json
        docente={}
        docente = {'nombres':'Javier','edad':23,'activo':True}
        edad=docente['edad']
        docente['edad']=24
        docente['carrera']='IS'
        # print(docente,edad,docente['edad'])
        # print(usuario,usuario[0], usuario[0:2],usuario[-1])
        # print(nombres,nombres[0], nombres[0:2],nombres[-1])
        print(materias,materias[2:],materias[:3], materias[::-1],materias[-2:])
        # #presentacion con format
        # print("""Mi nombre es {}, tengo {}
        #       años""".format(nombres,edad))
# print("sintaxis antes de instancia es: {}".format(sintaxis.instancia))        
ejer1=sintaxis() #instancia la clase sintaxis y crea el objeto ejer1(copia de la clase)
# print("sintaxis de ejer1 es: {}".format(sintaxis.instancia))
# ejer2=sintaxis("instancia2")
# print(ejer1.frase)
# print("sintaxis de ejer2 es: {}".format(sintaxis.instancia))
# print("sintaxis nuevamente ejer1 : {}".format(sintaxis.instancia))
# print(ejer2.frase)
ejer1.usoVariables()