class FuenteDeIones:
    def __init__(self, posicion, flujo_iones, metal_liquido):
        self.posicion = posicion
        self.flujo_iones = flujo_iones
        self.metal_liquido = metal_liquido

    def ajustar_flujo_iones(self, nuevo_flujo):
        self.flujo_iones = nuevo_flujo

    def cambiar_metal_liquido(self, nuevo_metal):
        self.metal_liquido = nuevo_metal

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

# Ejemplo de uso
if __name__ == "__main__":
    fuente_iones = FuenteDeIones(posicion=(0, 0, 1), flujo_iones=1e12, metal_liquido="Mercurio")
    print("Posición de la fuente de iones:", fuente_iones.posicion)
    print("Flujo de iones:", fuente_iones.flujo_iones)
    print("Metal líquido:", fuente_iones.metal_liquido)

    nuevo_flujo = 5e12
    fuente_iones.ajustar_flujo_iones(nuevo_flujo)
    print("Nuevo flujo de iones:", fuente_iones.flujo_iones)

    nuevo_metal = "Plata"
    fuente_iones.cambiar_metal_liquido(nuevo_metal)
    print("Nuevo metal líquido:", fuente_iones.metal_liquido)

    nueva_posicion = (0, 1, 0)
    fuente_iones.mover(nueva_posicion)
    print("Nueva posición de la fuente de iones:", fuente_iones.posicion)