class Empleado:
    __nombre: str
    __id: int
    __puesto: str

    def __init__(self, nombre: str, id: int, puesto: str):
        self.__nombre = nombre
        self.__id = id
        self.__puesto = puesto

    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__id

    def getPuesto(self):
        return self.__puesto

    def __str__(self):
        return f"Empleado: {self.__nombre}, ID: {self.__id}, Puesto: {self.__puesto}"
