class Electrodo:
    def __init__(self, posicion, potencial):
        self.posicion = posicion
        self.potencial = potencial

    def cambiar_potencial(self, nuevo_potencial):
        self.potencial = nuevo_potencial

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

# Ejemplo de uso
if __name__ == "__main__":
    electrodo = Electrodo(posicion=(0, 0, 0), potencial=100)
    print("Posición del electrodo:", electrodo.posicion)
    print("Potencial del electrodo:", electrodo.potencial)

    nuevo_potencial = 150
    electrodo.cambiar_potencial(nuevo_potencial)
    print("Nuevo potencial del electrodo:", electrodo.potencial)

    nueva_posicion = (0, 1, 0)
    electrodo.mover(nueva_posicion)
    print("Nueva posición del electrodo:", electrodo.posicion)