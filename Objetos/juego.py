#------------Clase Juego------------
import csv, operator

class Juego:
    
    #Cargar bancos de preguntas y respuestas
    def __init__(self, banco,rondas, tipo):
        self.banco     = banco # Bancos cargados en un archivo
        self.rondas    = rondas # Numero total de rondas
        self.nivel     = ["(Facil)", "(Intermedio)", "(Avanzado)", "(Experto)", "(Leyenda)"]
        self.categoria = ["Matemáticas", "Sistema Solar", "Capitales", "Historia", "Sofka"]
        self.valor     = [100, 200, 500, 1000, 5000]
        self.tipo      = tipo
        self.registro  = 'registro.csv'
        self.historial = {}
        # Contador auxiliar para manejo de listas
        self.aux = 0

    # Empezar el juego creando los objetos
    def iniciar(self):
        print("¡Bievenido al juego de Preguntas y Respuestas!")
        nombre = input("Digite su nombre: ")
        return nombre

    # Avanzar de ronda
    def avanzar(self):
        self.aux += 1
        return self.aux

    # Finalizar el juego y registrar resultado
    def finalizar(self, nombre, acumulado):
        print("-----------------------------------------------------------------")
        print("                     ¡Juego finalizado!")
        print("                      Nombre: ", nombre)
        print("                      Premio: ", acumulado)

        with open(self.registro, 'a', newline='') as archivo:
            escribir = csv.writer(archivo)
            escribir.writerow([nombre, acumulado])
                   
        with open(self.registro, 'r', newline='') as archivo: 
            leer = csv.reader(archivo)   
            print("-----------------------------------------------------------------")
            print("                  REGISTRO DE JUGADORES")
            for fila in leer:
                print("                  ", fila[0], "---", fila[1], self.tipo)
        print("-----------------------------------------------------------------")
