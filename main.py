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

# Realizar la pregunta de cada ronda
while ((pregunta.resultado == 2) and (juego.aux < 5)):
    # Establecer los datos de la ronda y mostrarlos
    ronda = Ronda(juego.aux, juego.nivel[juego.aux], juego.categoria[juego.aux], juego.valor[juego.aux])
    ronda.mostrardatos(tipo, premio.acumulado)
    # Elegir pregunta aleatoria, mostrar y validar respuesta del jugador
    pregunta.mostrar()
    pregunta.validar(jugador.responder())

    # Si el jugador se retira
    if pregunta.resultado == 1:
        jugador.retirar(premio.acumulado, tipo)
    # Si el jugador acierta
    elif pregunta.resultado == 2:
        premio.acumular(ronda.valor)
           # En la ronda final
        if ronda.numero == 5:
            juego.avanzar()
            jugador.ganar(premio.acumulado, tipo)
        # En una ronda cualquiera: Cambia el banco de preguntas
        else:
            pregunta.banco = bancos[juego.avanzar()]
    # Si el jugador falla
    else:
        jugador.perder()

juego.finalizar(jugador.nombre, jugador.puntaje)