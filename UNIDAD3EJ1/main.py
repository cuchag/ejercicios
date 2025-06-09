from gestorHotel import GestorHotel
from Hotel import Hotel
from Habitacion import Habitacion


def menu():
    op = None
    try:
        op = int(input("""Ingrese la opcion a ejecutar, 0 para finzalizar el programa: 
        1-Agregar habitacion
        2-Reservar habitacion
        3-Liberar habitacion
        4-Dado un tipo de habitacion, mostrar numero y piso de las habitaciones
        5-Mostrar habitaciones libres por piso
        6-Lista \n """))
    except ValueError:
        pass
    return op


if __name__ == "__main__":
    gestor = GestorHotel()
    gestor.cargaHoteles()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            i = int(input(
                "Ingrese hotel a agregarle habitacion:1 para hotel paraiso tropical-2 para hotel central "))
            i -= 1
            gestor.agregarHabitacionman(i)
        elif opcion == 2:
            intento = int(input("Ingrese numero de habitacion a reservar: \n"))
            gestor.reservarHabitacion(intento)
        elif opcion == 3:
            intento = int(input("Ingrese numero de habitacion a liberar: \n"))
            gestor.liberarHabitacion(intento)
        elif opcion == 4:
            tipo = input("Ingrese tipo de habitacion a buscar: \n")
            gestor.mostrarHabitacionesportipo(tipo)
        elif opcion == 5:
            piso = int(input("Ingrese piso a buscar: \n"))
            gestor.mostrarHabitacionesporpiso(piso)
        elif opcion == 6:
            gestor.mostrarHabitaciones()
        else:
            print("Opcion no valida, intente nuevamente.")
        opcion = menu()
