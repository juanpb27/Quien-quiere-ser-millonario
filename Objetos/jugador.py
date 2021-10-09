#-----------Clase Jugador------------

class Jugador:

    #Datos iniciales del jugador
    def __init__(self, nombre):
        self.nombre = nombre
        self.puntaje = 0

    def responder(self):
        respuesta = input("¿Cuál es su respuesta? Si desea retirarse con su acumulado, escriba la letra r: ").lower()
        return respuesta

    def retirar(self, acumulado, tipo):
        self.puntaje = acumulado
        print("\nBuena decision, aseguraste el acumulado de",self.puntaje,tipo)
    
    def ganar(self, acumulado,tipo):
        self.puntaje = acumulado
        print("\n¡¡¡FELICIDADES!!! HAS GANADO EL ACUMULADO DE",self.puntaje,tipo)

    def perder(self):
        self.puntaje = 0
        print("\nLo sentimos, has perdido todo. ¡Pero animate! Puedes volver a intentarlo en otra ocasion")