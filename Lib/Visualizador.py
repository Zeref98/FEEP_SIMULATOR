import matplotlib.pyplot as plt

class Visualizador:
    def __init__(self):
        pass

    def visualizar_trayectorias(self, particulas_simuladas):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        for particula in particulas_simuladas:
            x = [pos[0] for pos in particula.trayectoria]
            y = [pos[1] for pos in particula.trayectoria]
            z = [pos[2] for pos in particula.trayectoria]
            ax.plot(x, y, z)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.set_title('Trayectorias de partículas')
        plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de Visualizador
    visualizador = Visualizador()

    # Crear una lista de partículas simuladas (asumiendo que cada partícula tiene un atributo "trayectoria")
    particulas_simuladas = [...]

    # Visualizar las trayectorias de las partículas
    visualizador.visualizar_trayectorias(particulas_simuladas)
