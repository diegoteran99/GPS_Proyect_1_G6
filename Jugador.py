class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fichas = []
        
    def agregar_ficha(self, ficha):
        self.fichas.append(ficha)
        
    def mostrar_fichas(self):
        print(f"{self.nombre}: {self.fichas}")
    def mostrar_fichas(self):
        fichasString = ""
        for ficha in self.fichas:
            fichasString += f"{ficha} "
        
        print(f"{self.nombre}: {fichasString}")
        