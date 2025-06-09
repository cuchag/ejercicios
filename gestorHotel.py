import csv
from Hotel import Hotel
from Habitacion import Habitacion


class GestorHotel:
    __listahoteles: list

    def __init__(self):
        self.__listahoteles = []

    def agregarHotel(self, hotel: Hotel):
        self.__listahoteles.append(hotel)

    def cargaHoteles(self):
        i = 0
        archivo = open('Hoteles.csv')
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if len(fila) == 3:
                self.agregarHotel(Hotel(fila[0], fila[1], int(fila[2])))
                i += 1
            else:
                nro = int(fila[0])
                piso = int(fila[1])
                tipo = fila[2]
                precio = float(fila[3])
                if fila[4] == "True":
                    ocupada = True
                elif fila[4] == "False":
                    ocupada = False
                else:
                    ocupada = False
                self.__listahoteles[i -
                                    1].agregarHabitacion(nro, piso, tipo, precio, ocupada)
        archivo.close()

    def agregarHabitacionman(self, i):
        nro = int(input("Ingrese numero de habitacion: \n"))
        piso = int(input("Ingrese piso de habitacion: \n"))
        tipo = input("Ingrese tipo de habitacion: \n")
        precio = float(input("Ingrese precio de habitacion: \n"))
        ocupada = bool(
            input("Ingrese si la habitacion esta ocupada (True/False): \n"))
        self.__listahoteles[i].agregarHabitacion(
            nro, piso, tipo, precio, ocupada)

    def mostrarHabitaciones(self):
        for hotel in self.__listahoteles:
            print(f"Hotel: {hotel.getNombre()}")
            habitaciones = hotel.getListaHabitaciones()
            for habitacion in habitaciones:
                print(f"  Número: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}, Tipo: {habitacion.getTipo()}, Precio: {habitacion.getPrecio()}, Ocupada: {habitacion.getOcupada()}")

    def reservarHabitacion(self, intento):
        for hotel in self.__listahoteles:
            habitaciones = hotel.getListaHabitaciones()
            for habitacion in habitaciones:
                if habitacion.getNumero() == intento and not habitacion.getOcupada():
                    habitacion.setOcupada(True)
                    print(
                        f"Habitación {intento} reservada en {hotel.getNombre()}.")
                    return
        print(f"Habitación {intento} no encontrada o ya está ocupada.")

    def liberarHabitacion(self, intento):
        for hotel in self.__listahoteles:
            habitaciones = hotel.getListaHabitaciones()
            for habitacion in habitaciones:
                if habitacion.getNumero() == intento and habitacion.getOcupada() == True:
                    habitacion.setOcupada(False)
                    print(
                        f"Habitación {intento} liberada en {hotel.getNombre()}.")
                    return
        print(f"Habitación {intento} no encontrada o ya está ocupada.")

    def mostrarHabitacionesportipo(self, tipo):
        for hotel in self.__listahoteles:
            print(f"Hotel: {hotel.getNombre()}")
            habitaciones = hotel.getListaHabitaciones()
            for habitacion in habitaciones:
                if habitacion.getTipo() == tipo:
                    print(
                        f"  Número: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}, Tipo: {habitacion.getTipo()}, Precio: {habitacion.getPrecio()}, Ocupada: {habitacion.getOcupada()}")

    def mostrarHabitacionesporpiso(self, piso):
        for hotel in self.__listahoteles:
            print(f"Hotel: {hotel.getNombre()}")
            habitaciones = hotel.getListaHabitaciones()
            for habitacion in habitaciones:
                if habitacion.getPiso() == piso and not habitacion.getOcupada():
                    print(
                        f"  Número: {habitacion.getNumero()}, Piso: {habitacion.getPiso()}, Tipo: {habitacion.getTipo()}, Precio: {habitacion.getPrecio()}, Ocupada: {habitacion.getOcupada()}")
