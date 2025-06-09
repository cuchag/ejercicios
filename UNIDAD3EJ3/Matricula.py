from Empleados import Empleado
from Programa import Programa


class Matricula:
    __fecha: str
    __Empleado: Empleado
    __programa: Programa

    def __init__(self, fecha: str, empleado: Empleado, programa: Programa):
        self.__fecha = fecha
        self.__Empleado = empleado
        self.__programa = programa

    def get_fecha(self):
        return self.__fecha

    def get_empleado(self):
        return self.__Empleado

    def get_programa(self):
        return self.__programa

    def get_nombre_empleado(self):
        return self.__Empleado.getNombre()

    def get_nombre_programa(self):
        return self.__programa.get_nombre()
