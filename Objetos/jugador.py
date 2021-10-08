#-----------Clase Jugador------------

class Jugador():

    #Datos iniciales del jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def responder(self):
        respuesta = input("¿Cuál es su respuesta? Si desea retirarse escriba la letra r").lower()
        return respuesta

    def ganar(self):
        self.puntaje = Premio.acumulado
        Juego.finalizar()

    def perder(self):
        Juego.finalizar()
