from Jugador import Jugador
import random
fichas = ["[0;0]", "[1;1]", "[2;2]", "[3;3]", "[4;4]", "[5;5]", "[6;6]", "[0;1]", "[0;2]", "[0;3]", "[0;4]", "[0;5]", "[0;6]", "[1;2]", "[1;3]", "[1;4]", "[1;5]", "[1;6]", "[2;3]", "[2;4]", "[2;5]", "[2,6]", "[3;4]", "[3;5]", "[3;6]", "[4;5]", "[4;6]", "[5;6]"]
chanchos = ["[6;6]", "[5;5]", "[4;4]", "[3;3]", "[2;2]", "[1;1]", "[0;0]"]
random.shuffle(fichas)

def turno(posicion, ronda, cantJugadores):
    if posicion + ronda != 0:
        return (posicion + ronda) % cantJugadores
    else:
        return posicion

jugadores = []
#-----Crear jugadores y sus fichas
cantidadJugadores = int(input("Ingrese la cantidad de jugadores entre 2 y 14: "))
if cantidadJugadores >= 2 and cantidadJugadores <= 14:
    cantidadFichasJugador = len(fichas) // cantidadJugadores
    for i in range(cantidadJugadores):
        nuevoJugador = Jugador(f"Jugador {i + 1}")
        for i in range(cantidadFichasJugador):
            ficha = fichas.pop()
            nuevoJugador.agregar_ficha(ficha)
        jugadores.append(nuevoJugador)
print("")
for i in jugadores:
    i.mostrar_fichas()
print("")
#--------- 

encontrado = False  
for chancho in chanchos:
    if encontrado:
        break  
    for jugador in jugadores:
        if encontrado:
            break  
        for ficha in jugador.fichas:
            if chancho == ficha:
                turnoJugador = jugadores.index(jugador)
                print(f"Parte el {jugador.nombre} tiene el chancho {ficha}")
                input("")
                encontrado = True  
                break  
            
finalizado = False
ronda = 0
juego = []
#while finalizado != True:
    
###--------Primera jugada
jugadorActual = jugadores[turno(turnoJugador,ronda,cantidadJugadores)]
mostrarJugador = jugadorActual.mostrar_fichas()
input("")
fichaJugada = ficha
jugadorActual.fichas.remove(fichaJugada)
juego.append(fichaJugada)
print(f"juego: {juego}")
input("")
ronda += 1

###-----

###----Segunda jugada
jugadorActual = jugadores[turno(turnoJugador,ronda,cantidadJugadores)]
mostrarJugador = jugadorActual.mostrar_fichas()
input("")
numeroFicha = juego[0][1]
print(numeroFicha)
for ficha in jugadorActual.fichas:
    if juego[0][1] in ficha:
        if ficha[3] == numeroFicha:
            fichaJugada = f"[{ficha[3]};{ficha[1]}]"
        else:
            fichaJugada = ficha
        jugadorActual.fichas.remove(ficha)
        juego.append(fichaJugada)
        break
print(f"juego: {juego}")
input("")
ronda += 1
###---------


