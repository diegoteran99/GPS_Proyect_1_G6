from Jugador import Jugador
import random

fichas = ["[0;0]", "[1;1]", "[2;2]", "[3;3]", "[4;4]", "[5;5]", "[6;6]", "[0;1]", "[0;2]", "[0;3]", "[0;4]", "[0;5]", "[0;6]", "[1;2]", "[1;3]", "[1;4]", "[1;5]", "[1;6]", "[2;3]", "[2;4]", "[2;5]", "[2,6]", "[3;4]", "[3;5]", "[3;6]", "[4;5]", "[4;6]", "[5;6]"]
jugadores = []
random.shuffle(fichas)
#-----Crear jugadores y sus fichas
cantidadJugadores = int(input("Ingrese la cantidad de jugadores entre 2 y 14: "))
if cantidadJugadores >= 2 and cantidadJugadores <= 14:
    cantidadFichas = len(fichas) // cantidadJugadores
    for i in range(cantidadJugadores):
        nuevoJugador = Jugador(f"Jugador {i + 1}")
        for i in range(cantidadFichas):
            ficha = fichas.pop()
            nuevoJugador.agregar_ficha(ficha)
        jugadores.append(nuevoJugador)
#---------        
for i in jugadores:
    i.mostrar_fichas()
