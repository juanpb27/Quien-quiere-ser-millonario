#-----------Clase Premio------------

class Premio:

    #Se define el tipo de premio y el valor acumulado
    def __init__(self, tipo):
        self.tipo = tipo
        self.acumulado = 0

    def acumular(self):
        self.acumulado += Ronda.valor