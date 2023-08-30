from Jugador import Jugador
import random

chanchos = ["[6;6]", "[5;5]", "[4;4]", "[3;3]", "[2;2]", "[1;1]", "[0;0]"]
fichas = chanchos + ["[0;1]", "[0;2]", "[0;3]", "[0;4]", "[0;5]", "[0;6]", "[1;2]", "[1;3]", "[1;4]", "[1;5]", "[1;6]", "[2;3]", "[2;4]", "[2;5]", "[2,6]", "[3;4]", "[3;5]", "[3;6]", "[4;5]", "[4;6]", "[5;6]"]
random.shuffle(fichas)
finalizado = False
ronda = 0
juego = []
    
def turno_actual(posicion, ronda, cantJugadores):
    if posicion + ronda != 0:
        return (posicion + ronda) % cantJugadores
    else:
        return posicion

jugadores = []
#-----Crear jugadores y sus fichas
while True:
    inputValue = input("Ingrese la cantidad de jugadores entre 2 y 14: ")
    if inputValue.isnumeric():
        cantidadJugadores = int(inputValue)
        if cantidadJugadores >= 2 and cantidadJugadores <= 14:
            cantidadFichasJugador = len(fichas) // cantidadJugadores
            for i in range(cantidadJugadores):
                nuevoJugador = Jugador(f"Jugador {i + 1}")
                for i in range(cantidadFichasJugador):
                    ficha = fichas.pop()
                    nuevoJugador.agregar_ficha(ficha)
                jugadores.append(nuevoJugador)
            break
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
                print(f"Parte el {jugador.nombre} tiene el chancho {ficha[1]}")
                input("")
                encontrado = True  
                break  
            
###--------Primera jugada
jugadorActual = jugadores[turno_actual(turnoJugador,ronda,cantidadJugadores)]
mostrarJugador = jugadorActual.mostrar_fichas()
input("")
fichaJugada = ficha
jugadorActual.fichas.remove(fichaJugada)
juego.append(fichaJugada)
print(f"juego: {juego}")
input("")
ronda += 1
###-----
skippedCount=0
###---Resto jugadas
while finalizado != True:
    if skippedCount == cantidadJugadores:
        finalizado = True
        print("Fin del juego")
        break
    jugadorActual = jugadores[turno_actual(turnoJugador,ronda,cantidadJugadores)]
    mostrarJugador = jugadorActual.mostrar_fichas()
    input("")
    primeraFicha, ultimaFicha = juego[0], juego[-1]
    for ficha in jugadorActual.fichas:
        if ultimaFicha[3] in ficha:
            if ficha[3] == ultimaFicha[3]:
                fichaJugada = f"[{ficha[3]};{ficha[1]}]"
            else:
                fichaJugada = ficha
            jugadorActual.fichas.remove(ficha)
            juego.append(fichaJugada)
            if jugadorActual.fichas == []:
                finalizado = True
                print(f"Fin del juego, ganador {jugadorActual.nombre}")
                break
            skippedCount=0
            break
        if primeraFicha[1] in ficha:
            if ficha[1] == primeraFicha[1]:
                fichaJugada = f"[{ficha[3]};{ficha[1]}]"
            else:
                fichaJugada = ficha
            jugadorActual.fichas.remove(ficha)
            juego.insert(0,fichaJugada)
            if jugadorActual.fichas == []:
                finalizado = True
                print(f"Fin del juego, ganador {jugadorActual.nombre}")
                break
            skippedCount=0
            break
        if ultimaFicha[3] not in ficha and primeraFicha[1] not in ficha:
            fichaJugada = "paso"
            print (f"{jugadorActual.nombre} paso")
            skippedCount+=1
            break
    print(f"juego: {juego}")
    input("")
    ronda += 1     
#falta agregar cuando pierden
        
