#-----------Clase Pregunta------------
from .juego import Juego
import random

class Preguntas(Juego):

    #Carga del banco de preguntas
    def __init__(self, banco):
        super().__init__(Jugador, Preguntas, Premio, Ronda)
        self.banco  = banco  #Banco de preguntas actual
        self.eleccion = {}   #Pregunta elegida en cada ronda


    def mostrar(self):
        self.eleccion = random.choice(self.banco)
        print("Premio: ", self.ronda.valor, self.premio.tipo)
        print("Pregunta: ", self.eleccion.get('pregunta'))
        print("Opciones: ", self.eleccion.get('opciones'))

    def validar(self):
        # Si el jugador se retira
        if Jugador.responder() == 'r':
            Jugador.ganar()
        
        # Si el jugador acierta
        elif Jugador.responder() == self.eleccion.get('respuesta'):
            # Si acierta la ronda final
            if Ronda.numero == self.r:
                Jugador.ganar()
            # Si acierta una ronda diferente
            else:
                print("¡Respuesta correcta!")
                Juego.avanzar()
        
        # Si el jugador falla
        else:
            print("¡Respuesta incorrecta!")
            Jugador.perder()
            Juego.finalizar()
        