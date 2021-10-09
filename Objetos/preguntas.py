#-----------Clase Pregunta------------
import random

class Preguntas:

    # Carga del banco de preguntas
    def __init__(self, banco):
        self.banco  = banco  # Banco de preguntas actual
        self.eleccion = {}   # Pregunta elegida en cada ronda
        self.resultado = 2  # 1-Retira ; 2-Acierto ; 3-Fallo

    # Mostrar las preguntas escogidas aleatoriamente y sus respectivas opciones
    def mostrar(self):
        self.eleccion = random.choice(self.banco)
        print("\nPregunta: ", self.eleccion.get('pregunta'))
        print("Opciones: ", self.eleccion.get('opciones'),"\n")

    # Validar la respuesta del jugador
    def validar(self,respuesta):
        # Si el jugador se retira
        if respuesta == 'r':
            self.resultado = 1
        
        # Si el jugador acierta
        elif respuesta == self.eleccion.get('respuesta'):
            print("¡Respuesta correcta!")
            self.resultado = 2
        
        # Si el jugador falla
        else:
            print("¡Respuesta incorrecta!")
            self.resultado = 3