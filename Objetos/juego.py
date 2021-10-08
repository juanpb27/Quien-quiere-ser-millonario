"""------------Clase Juego------------
Se importan los métodos de otros objetos
"""
from .jugador import Jugador
from .preguntas import Preguntas
from .premio import Premio
from .ronda import Ronda

class Juego(Jugador, Preguntas, Premio, Ronda):
    
    #Cargar bancos de preguntas y respuestas
    def __init__(self, banco,rondas, tipo):
        self.banco = banco # Bancos cargados en un archivo
        self.rondas = rondas # Numero total de rondas
        self.nivel = ["Facil", "Intermedio", "Avanzado", "Experto", "Leyenda"]
        self.categoria = ["1", "2", "3", "4", "5"]
        self.valor = [100, 200, 500, 1000, 5000]
        self.tipo = tipo
        # Contador auxiliar para manejo de listas
        self.aux = 0


    # Empezar el juego creando los objetos
    def iniciar(self):
        print("¡Bievenido al juego de Preguntas y Respuestas! \n")
        nombre    = input("Digite su nombre: ")
        self.jugador   = Jugador(nombre)
        self.ronda     = Ronda(self.aux, self.nivel[self.aux], self.categoria[self.aux], self.valor[self.aux])
        self.preguntas = Preguntas(self.banco[self.aux])
        self.premio    = Premio(self.tipo)
        self.preguntar()
        
    # Realizar la pregunta de la ronda
    def preguntar(self):
        self.ronda.mostrardatos(self.tipo)
        self.preguntas.mostrar()
        self.jugador.responder()
        self.preguntas.validar()

    # Avanzar de ronda
    def avanzar(self):
        self.aux += 1
        Premio.acumular()

    # Finalizar el juego por retiro o respuesta incorrecta - Guardar datos
    def finalizar(self):
        print("¡Juego finalizado!")
        print("Nombre: ", Jugador.nombre)
        print("Premio: ", Premio.acumulado)
