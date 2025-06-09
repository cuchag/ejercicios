class Programa:
    __nombre: str
    _codigo: str
    __duracion: int

    def __init__(self, nombre: str, codigo: int, duracion: int):
        self.__nombre = nombre
        self._codigo = codigo
        self.__duracion = duracion

    def get_nombre(self):
        return self.__nombre

    def get_codigo(self):
        return self._codigo

    def get_duracion(self):
        return self.__duracion

    def __str__(self):
        return f"Programa: {self.__nombre}, Código: {self._codigo}, Duración: {self.__duracion} meses"
