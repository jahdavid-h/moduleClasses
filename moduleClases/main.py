# main.py
from ciclismo import Ciclista

def main():
    # Crear un objeto de la clase Ciclista
    ciclista = Ciclista(nombre="Nathan", distancia=50, horas=2)

    # Mostrar la información del ciclista
    print(ciclista)

    # Calcular y mostrar la velocidad promedio
    velocidad = ciclista.calcular_velocidad()
    print(f"Velocidad promedio: {velocidad} km/h")

    # Calcular y mostrar la cantidad de agua que debe consumir
    hidratacion = ciclista.calcular_hidratacion()
    print(f"Agua recomendada: {hidratacion} litros")

if __name__ == "__main__":
    main()

from bestPracticesOOP import Alumno

def main():
    registro_alumnos = {}

    # Capturar 3 registros
    for i in range(3):
        alumno1 = Alumno()
        print("          Ingrese los datos corespondientes")
        alumno1.set_nombre(input(f"Ingrese el nombre del alumno {i}: "))
        alumno1.set_apellido_paterno(input(f"Ingrese el apellido paterno del alumno {i}: "))
        alumno1.set_apellido_materno(input(f"Ingrese el apellido materno del alumno {i}: "))
        alumno1.set_no_control(input(f"Ingrese el número de control del alumno {i}: "))
        alumno1.set_semestre(input(f"Ingrese el semestre del alumno {i}: "))
        print()

        registro_alumnos[f"alumno1_{i}"] = alumno1

    # Mostrar los nombres de los registros
    for i in range(3):
        alumno1 = registro_alumnos[f"alumno1_{i}"]
        print("          Datos Ingresados")
        print(f"Alumno {i} ")
        print(f"Nombre Completo: {alumno1.get_nombrecom()}")
        print(f"No. de Control: {alumno1.get_no_control()}")
        print(f"Semestre: {alumno1.get_semestre()}")
        print()

if __name__ == "__main__":
    main()