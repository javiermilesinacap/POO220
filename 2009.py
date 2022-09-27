from datetime import datetime
print(f"Este es un programa de un vehículo"+ str(datetime.now()))
#ruedas, ubicación, puertas, estado 
estado = False
ruedas = input("Cuántas ruedas tiene el vehículo?")
ubicacion = input("Cuál es la ubicación actual del vehículo?")
velocidad = input("Cuál es la velocidad del vehículo?")
def encender():
    global estado
    estado = not(estado)
    print("---encendido----" if estado else "----apagado----") 
def salida():
    print("El vehículo tiene "+str(ruedas)+ "ruedas")
    print("El vehículo está en la pos "+str(ubicacion)+ " GPS")
    print("El vehículo va a "+str(velocidad)+ " km/h")
def acelerar():
    global velocidad
    global estado
    if(estado):
        velocidad=int(velocidad)+10
        print("El vehículo ha acelerado a "+str(velocidad)+ " km/h")
        salida()
    else:
        print("Encienda el vehiculo primero")
opc = 0
print("Elija qué desea realizar.")
while((opc)!=9):
    opc = int(input("1.- Mostrar Veh \n 2.- Acelerar \n 3.- encender \n 9.- Salir"))
    if(opc==1):
        salida()
    elif(opc==2):
        acelerar()
    elif(opc==3):
        encender()
    
print("Buen viaje")