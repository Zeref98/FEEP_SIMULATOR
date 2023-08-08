class CampoMagnetico:
    def __init__(self, intensidad, direccion):
        self.intensidad = intensidad
        self.direccion = direccion

    def ajustar_intensidad(self, nueva_intensidad):
        self.intensidad = nueva_intensidad

    def cambiar_direccion(self, nueva_direccion):
        self.direccion = nueva_direccion

# Ejemplo de uso
if __name__ == "__main__":
    campo_magnetico = CampoMagnetico(intensidad=0.5, direccion=(0, 0, 1))
    print("Intensidad del campo magnético:", campo_magnetico.intensidad)
    print("Dirección del campo magnético:", campo_magnetico.direccion)

    nueva_intensidad = 0.8
    campo_magnetico.ajustar_intensidad(nueva_intensidad)
    print("Nueva intensidad del campo magnético:", campo_magnetico.intensidad)

    nueva_direccion = (1, 0, 0)
    campo_magnetico.cambiar_direccion(nueva_direccion)
    print("Nueva dirección del campo magnético:", campo_magnetico.direccion)