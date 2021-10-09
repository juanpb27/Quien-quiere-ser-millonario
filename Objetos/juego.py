#------------Clase Juego------------

class Juego:
    
    #Cargar bancos de preguntas y respuestas
    def __init__(self, banco,rondas, tipo):
        self.banco     = banco # Bancos cargados en un archivo
        self.rondas    = rondas # Numero total de rondas
        self.nivel     = ["(Facil)", "(Intermedio)", "(Avanzado)", "(Experto)", "(Leyenda)"]
        self.categoria = ["1", "2", "3", "4", "5"]
        self.valor     = [100, 200, 500, 1000, 5000]
        self.tipo      = tipo
        # Contador auxiliar para manejo de listas
        self.aux = 0


    # Empezar el juego creando los objetos
    def iniciar(self):
        print("¡Bievenido al juego de Preguntas y Respuestas! \n")
        nombre = input("Digite su nombre: ")
        return nombre

    # Avanzar de ronda
    def avanzar(self):
        self.aux += 1

    # Finalizar el juego por retiro o respuesta incorrecta - HACE FALTA QUE GUARDE LOS DATOS
    def finalizar(self, nombre, acumulado):
        print("¡Juego finalizado!")
        print("Nombre: ", nombre)
        print("Premio: ", acumulado)
