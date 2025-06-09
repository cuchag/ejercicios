from Habitacion import Habitacion


class Hotel:
    __nombre: str
    __direccion: str
    __telefono: str
    __listaHabitaciones: list

    def __init__(self, nombre: str, direccion: str, telefono: str):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__listaHabitaciones = []

    def agregarHabitacion(self, nro: int, piso: int, tipo: str, precio: float, ocupada: bool):
        habitacion = Habitacion(nro, piso, tipo, precio, ocupada)
        self.__listaHabitaciones.append(habitacion)

    def getNombre(self):
        return self.__nombre

    def getDireccion(self):
        return self.__direccion

    def getTelefono(self):
        return self.__telefono

    def getListaHabitaciones(self):
        return self.__listaHabitaciones
