print("Hola Mundo")
lista = [22,44,1.2,"Hola", 'Mundo']
tupla= (22,44,1.2,"Hola", 'Mundo')
print(lista)
print(tupla)
lista.append("INSERTANDO")
print(lista)
lista.insert(2,"POSICION 2")
print(lista)
unavariable = {"a":123,"b":"cdef", "curso":"fghi", "rut":999}
unavariable["edad"] = 99
print(unavariable)
#creando un conjunto de personas
#comentario
conjunto = []
i=0
while i<3:
    print(i)
    i = i+1
    persona1 = {}
    #persona1 = {"nombre":"juan"+str(i), "apellido":"perez"+str(i)}
    persona1["nombre"] = input("Escribe el nombre")
    persona1["apellido"] = input("Escribe el apellido")
    conjunto.append(persona1)
print(conjunto)
print(conjunto[0]["nombre"])
for z in conjunto:
    print(z["nombre"]+" "+z["apellido"])