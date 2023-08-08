##DEPRECATED IN PROCESS

class InterfazUsuario:
    def __init__(self, simulacion, visualizador, optimizador):
        self.simulacion = simulacion
        self.visualizador = visualizador
        self.optimizador = optimizador

    def ejecutar(self):
        while True:
            print("1. Simular")
            print("2. Visualizar")
            print("3. Optimizar")
            print("4. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.realizar_simulacion()
            elif opcion == "2":
                self.visualizar_resultados()
            elif opcion == "3":
                self.optimizar_posicion_electrodos()
            elif opcion == "4":
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, elige una opción válida.")

    def realizar_simulacion(self):
        # Lógica para configurar y realizar la simulación
        pass

    def visualizar_resultados(self):
        # Lógica para visualizar los resultados de la simulación
        pass

    def optimizar_posicion_electrodos(self):
        # Lógica para realizar la optimización de la posición de los electrodos
        pass

# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de SimulacionFEEP, SimulacionLMIS, Visualizador, Optimizador
    simulacion =...
    visualizador =...
    optimizador =...
    
    # Crear una instancia de InterfazUsuario con las instancias anteriores
    interfaz = InterfazUsuario(simulacion, visualizador, optimizador)

    # Ejecutar la interfaz de usuario
    interfaz.ejecutar()
