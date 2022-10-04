#Variables
a = 123
b = "hola mundo"
#Funciones
def mensaje():
    print("Esto es un mensaje")
def mensaje1():
    print("Esto es una variable"+b)
mensaje()
mensaje1()
#DESDE ACA COMIENZA LA LECCION DE CLASES.
class UnaClase:
    atributo = 123
    atributo2 = 456
class Persona: 
    nombre = ""
    def mostrarNombre(self):
        print("Mi nombre es: "+self.nombre)
    def mostrarDatos(self):
        print("La persona se llama "+ str(self.nombre) + "de edad:"+ str(self.edad))
    def __init__(self, nombre ="", edad=0):
        self.edad = edad
        self.nombre = nombre
objeto1 = UnaClase()
objeto2 = UnaClase()
objeto1.atributo = 999
objeto2.atributo = 888
persona1 = Persona()
persona1.nombre = "Benjamin"
persona2 = Persona()
persona2.nombre = "Miguel"
print("Existen dos personas: "+ persona1.nombre +" y "+persona2.nombre)
print("LA edad de la persona 1 es: "+ str(persona1.edad))
persona1.mostrarNombre()
persona2.mostrarNombre()
print(persona1)
persona3 = Persona(22,"Juan")
persona3.mostrarDatos()