#-----------Clase Pregunta------------
import random

class Preguntas:

    #Carga del banco de preguntas
    def __init__(self, banco):
        self.banco  = banco  #Banco de preguntas actual
        self.eleccion = {}   #Pregunta elegida en cada ronda
        self.acierta = True  #Condicion para avanzar de ronda


    def mostrar(self):
        self.eleccion = random.choice(self.banco)
        print("Pregunta: ", self.eleccion.get('pregunta'))
        print("Opciones: ", self.eleccion.get('opciones'))

    def validar(self,respuesta):
        # Si el jugador se retira
        if respuesta == 'r':
            self.acierta = False
        
        # Si el jugador acierta
        elif respuesta == self.eleccion.get('respuesta'):
            print("¡Respuesta correcta!")
            self.acierta = True
        
        # Si el jugador falla
        else:
            print("¡Respuesta incorrecta!")
            self.acierta = False
        