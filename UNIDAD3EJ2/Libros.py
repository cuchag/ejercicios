class Libro:
    __titulo: str
    __autor: str
    __numero: str
    __genero: str

    def __init__(self, titulo: str, autor: str, numero: str, genero: str):
        self.__titulo = titulo
        self.__autor = autor
        self.__numero = numero
        self.__genero = genero

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getNumero(self):
        return self.__numero

    def getGenero(self):
        return self.__genero

    def __str__(self):
        return f"Titulo: {self.__titulo}, Autor: {self.__autor}, Numero: {self.__numero}, Genero: {self.__genero}"
