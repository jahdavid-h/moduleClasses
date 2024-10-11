# ciclismo.py
class Ciclista:
    def __init__(self, nombre, distancia, horas):
        self.__nombre = nombre
        self.distancia = distancia  # en kilómetros
        self.horas = horas  # tiempo en horas

    def calcular_velocidad(self):
        # Calcula la velocidad promedio en km/h
        if self.horas > 0:
            return self.distancia / self.horas
        else:
            return 0

    def calcular_hidratacion(self):
        # Asume que se necesitan 0.5 litros de agua por hora de ciclismo
        return 0.5 * self.horas

    def __str__(self):
        return f"Ciclista: {self.__nombre}, Distancia: {self.distancia} km, Tiempo: {self.horas} horas"
