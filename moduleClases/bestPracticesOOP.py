
class Alumno:
    #Crear una funcion conturctor con atributos vacios
    def __init__(self):
        # Atributos privados
        self.__nombre = ""
        self.__apellido_paterno = ""
        self.__apellido_materno = ""
        self.__no_control = ""
        self.__semestre = ""

    # Métodos para establecer los valores (setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido_paterno(self, apellido_paterno):
        self.__apellido_paterno = apellido_paterno

    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno

    def set_no_control(self, no_control):
        self.__no_control = no_control

    def set_semestre(self, semestre):
        self.__semestre = semestre

    # Métodos para obtener los valores (getters)
    def get_nombre(self):
        return self.__nombre

    def get_apellido_paterno(self):
        return self.__apellido_paterno

    def get_apellido_materno(self):
        return self.__apellido_materno

    def get_no_control(self):
        return self.__no_control

    def get_semestre(self):
        return self.__semestre
    def get_nombrecom(self):
        return self.__apellido_paterno + " " + self.__apellido_materno + " " + self.__nombre
