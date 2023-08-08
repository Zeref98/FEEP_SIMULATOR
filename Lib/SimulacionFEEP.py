from Lib.Particula import Particula
from Lib.Electrodo import Electrodo
from Lib.FuenteDeIones import FuenteDeIones
from Lib.CampoMagnetico import CampoMagnetico


class SimulacionFEEP:
    def __init__(self, electrodo, fuente_iones, campo_magnetico):
        self.electrodo = electrodo
        self.fuente_iones = fuente_iones
        self.campo_magnetico = campo_magnetico

    def simular(self, tiempo_simulacion, paso_tiempo):
        # Inicializar variables y listas para almacenar resultados
        tiempo_actual = 0
        particulas_simuladas = []

        while tiempo_actual <= tiempo_simulacion:
            # Simular generación de iones y aceleración
            for _ in range(self.fuente_iones.flujo_iones):
                nueva_particula = Particula(
                    posicion=self.fuente_iones.posicion,
                    velocidad=(0, 0, 0),
                    carga=self.fuente_iones.carga_ion,
                    masa=self.fuente_iones.masa_ion
                )
                # Aplicar aceleración a la partícula según el campo eléctrico
                aceleracion = calcular_aceleracion(self.electrodo.potencial, nueva_particula.carga, nueva_particula.masa)
                nueva_particula.velocidad = (
                    nueva_particula.velocidad[0] + aceleracion[0] * paso_tiempo,
                    nueva_particula.velocidad[1] + aceleracion[1] * paso_tiempo,
                    nueva_particula.velocidad[2] + aceleracion[2] * paso_tiempo
                )
                particulas_simuladas.append(nueva_particula)

            tiempo_actual += paso_tiempo

        return particulas_simuladas
    def generar_particulas_iones(self):
        # Simular la emisión de iones desde la fuente
        # Puedes aplicar aquí lógica más compleja para modelar la emisión de campo
        pass

    def acelerar_particula(self, particula, paso_tiempo):
        # Calcular la fuerza eléctrica y magnética sobre la partícula
        # Actualizar la velocidad y posición de la partícula según las fuerzas
        pass

def calcular_aceleracion(potencial, carga, masa):
    # Calcula la aceleración de una partícula en función del potencial, carga y masa
    aceleracion = carga * potencial / masa
    return (0, 0, aceleracion)



# Ejemplo de uso
if __name__ == "__main__":
    electrodo = Electrodo(posicion=(0, 0, 0), potencial=100)
    fuente_iones = FuenteDeIones(posicion=(0, 0, 1), flujo_iones=1000, carga_ion=1.6e-19, masa_ion=1.67e-27)
    campo_magnetico = CampoMagnetico(intensidad=0.5, direccion=(0, 0, 1))

    simulacion_fEEP = SimulacionFEEP(electrodo, fuente_iones, campo_magnetico)
    resultados_simulacion = simulacion_fEEP.simular(tiempo_simulacion=0.001, paso_tiempo=0.00001)

    for particula in resultados_simulacion:
        print("Posición de la partícula:", particula.posicion)
        print("Velocidad de la partícula:", particula.velocidad)