import math
import pygame
class Vehiculo:
    def __init__(self,velocidad=0, lat=0.0, lon=300.0):
        self.velocidad = velocidad
        self.lat = lat
        self.lon = lon
        self.distancia = 0
    def __str__(self) -> str:
        return(str(self.velocidad))
    def __repr__(self):
        return f'Vehiculo({self.velocidad})'
    def acelerar(self):
        self.velocidad += 10
        self.lat += 5
        self.__str__()
    def frenar(self):
        self.velocidad -=10
        self.lat -= 5
        self.__str__()
    def avanzar(self):
        self.distancia += 10 + (self.velocidad/10 * self.distancia)
    def setVelocidad(self,velocidad):
        self.velocidad = velocidad
    def getVelocidad(self):
        return self.velocidad
    def GPS(self):
        latD = float(input("Ingrese lat destino en decimal"))
        lonD = float(input("Ingrese lon destino en decimal"))
        circunf = math.pi * latD * 2
class Carretera: 
    velocidad = 0
    def __init__(self, velocidad=0) -> None:
        self.velocidad = velocidad
    def getVelocidad(self):
        return self.velocidad
    def setVelocidad(self,velocidad):
        self.velocidad = velocidad

objeto = Vehiculo()
fondo = Carretera()
pygame.init()
ventana = pygame.display.set_mode((800,600))
autito = pygame.image.load("./car.png").convert_alpha()
carretera = pygame.image.load("./fondo.png").convert_alpha()
repr(objeto)
while(True):
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_w):
            objeto.acelerar()
            
            print("la velocidad del vehiculo es: "+objeto.velocidad.__str__())
        if(event.type == pygame.KEYDOWN and event.key == pygame.K_s):
            objeto.frenar()
            
            print("la velocidad del vehiculo es: "+objeto.velocidad.__str__())

        ventana.fill((255,255,255))
        ventana.blit(carretera,(fondo.velocidad,0))
        ventana.blit(autito,(objeto.lat,objeto.lon))
    fondo.velocidad -= (objeto.velocidad/5)
    pygame.display.update()
            
    if(fondo.velocidad<-300):
        fondo.velocidad=0