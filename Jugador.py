class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fichas = []
        
    def agregar_ficha(self, ficha):
        self.fichas.append(ficha)
        
    def mostrar_fichas(self):
        print(f"{self.nombre}: {self.fichas}")
        