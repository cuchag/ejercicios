class Habitacion:
    __numero = int
    __piso = int
    __tipo = str
    __precio = float
    __ocupada = bool

    def __init__(self, numero: int, piso: int, tipo: str, precio: float, ocupada: bool):
        self.__numero = numero
        self.__piso = piso
        self.__tipo = tipo
        self.__precio = precio
        self.__ocupada = ocupada

    def getNumero(self):
        return self.__numero

    def getPiso(self):
        return self.__piso

    def getTipo(self):
        return self.__tipo

    def getPrecio(self):
        return self.__precio

    def getOcupada(self):
        return self.__ocupada

    def setOcupada(self, ocupada: bool):
        self.__ocupada = ocupada
