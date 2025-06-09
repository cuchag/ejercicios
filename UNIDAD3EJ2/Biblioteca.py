class Biblioteca:
    __nombre: str
    __direccion: str
    _telefono: str
    __libros: list

    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self._telefono = telefono
        self.__libros = []

    def agregarLibro(self, libro):
        self.__libros.append(libro)

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self._telefono

    def getLibros(self):
        return self.__libros

    def __str__(self):
        return f"Nombre: {self.__nombre}, Direccion: {self.__direccion}, Telefono: {self._telefono}"
