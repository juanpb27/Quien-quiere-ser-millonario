#-----------Clase Ronda------------

class Ronda:
    
    #Datos importantes de cada ronda
    def __init__(self, numero, nivel, categoria, valor):
        self.numero = numero + 1
        self.nivel = nivel
        self.categoria = categoria
        self.valor = valor

    def mostrardatos(self, tipo):
        print("\nRonda ", self.numero, self.nivel)
        print("Categoria: ", self.categoria)
        print("Premio de la ronda: ", self.valor, tipo)
