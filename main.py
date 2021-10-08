#Configuracion inicial

# Modulos y archivos necesarios
from banco import banco1, banco2, banco3, banco4, banco5
from Objetos.juego import Juego
# Numero de rondas
rds = 5
# Bancos
bancos = [banco1, banco2, banco3, banco4, banco5]
# Tipo de premio (puntos/dinero)
tipo = " puntos"

# Inicio del juego
juego = Juego(bancos, rds, tipo)
juego.iniciar()