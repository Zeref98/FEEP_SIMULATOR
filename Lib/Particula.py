class Particula:
    def __init__(self, posicion, velocidad, carga, masa):
        self.posicion = posicion
        self.velocidad = velocidad
        self.carga = carga
        self.masa = masa

    def actualizar_posicion(self, delta_t):
        nueva_posicion = (
            self.posicion[0] + self.velocidad[0] * delta_t,
            self.posicion[1] + self.velocidad[1] * delta_t,
            self.posicion[2] + self.velocidad[2] * delta_t
        )
        self.posicion = nueva_posicion

# Ejemplo de uso
if __name__ == "__main__":
    posicion_inicial = (0, 0, 0)
    velocidad_inicial = (100, 0, 0)
    carga = 1.6e-19  # Carga de un protón en Coulombs
    masa = 1.67e-27  # Masa de un protón en kg

    particula = Particula(posicion=posicion_inicial, velocidad=velocidad_inicial, carga=carga, masa=masa)
    print("Posición inicial:", particula.posicion)
    print("Velocidad inicial:", particula.velocidad)
    print("Carga de la partícula:", particula.carga)
    print("Masa de la partícula:", particula.masa)

    delta_t = 0.001  # Intervalo de tiempo para actualizar la posición
    particula.actualizar_posicion(delta_t)
    print("Nueva posición después de un intervalo de tiempo:", particula.posicion)