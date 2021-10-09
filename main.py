# Modulos y archivos necesarios
from banco import banco1, banco2, banco3, banco4, banco5
from Objetos.juego import Juego
from Objetos.jugador import Jugador
from Objetos.ronda import Ronda
from Objetos.preguntas import Preguntas
from Objetos.premio import Premio
# Numero de rondas
rds = 5
# Bancos
bancos = [banco1, banco2, banco3, banco4, banco5]
# Tipo de premio (puntos/dinero)
tipo = "puntos"
# Creacion de algunos objetos e inicio del juego
juego    = Juego(bancos, rds, tipo)
jugador  = Jugador(juego.iniciar())
pregunta = Preguntas(bancos[juego.aux])
premio   = Premio(tipo)

# Realizar la pregunta de la ronda
while ((pregunta.acierta == True) and (juego.aux < 5)):
    ronda = Ronda(juego.aux, juego.nivel[juego.aux], juego.categoria[juego.aux], juego.valor[juego.aux])
    ronda.mostrardatos(tipo)
    pregunta.mostrar()
    pregunta.validar(jugador.responder())
    juego.avanzar()