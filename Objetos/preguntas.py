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
        print("Opciones:   a)", self.eleccion.get('opciones').get('a'))
        print("            b)", self.eleccion.get('opciones').get('b'))
        print("            c)", self.eleccion.get('opciones').get('c'))
        print("            d)", self.eleccion.get('opciones').get('d'))

    # Validar la respuesta del jugador
    def validar(self,respuesta):
        # Si el jugador se retira
        if respuesta == 'r':
            self.resultado = 1
            print("La respuesta era", self.eleccion.get('respuesta'), ")",
             self.eleccion.get('opciones').get(self.eleccion.get('respuesta')))
        
        # Si el jugador acierta
        elif respuesta == self.eleccion.get('respuesta'):
            self.resultado = 2
            print("¡Respuesta correcta!")
        
        # Si el jugador falla
        else:
            self.resultado = 3
            print("¡Respuesta incorrecta! La respuesta es", self.eleccion.get('respuesta'), ")",
             self.eleccion.get('opciones').get(self.eleccion.get('respuesta')))