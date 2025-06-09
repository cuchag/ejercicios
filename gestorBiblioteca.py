import csv
from Biblioteca import Biblioteca
from Libros import Libro


class gestorBiblioteca:
    __listaB: list

    def __init__(self):
        self.__listaB = []

    def agregarBiblioteca(self, biblioteca: Biblioteca):
        self.__listaB.append(biblioteca)

    def cargarDatos(self):
        i = 0
        archivo = open("Biblioteca.csv")
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            if len(fila) == 3:
                nombre = fila[0]
                direccion = fila[1]
                telefono = fila[2]
                b = Biblioteca(nombre, direccion, telefono)
                self.agregarBiblioteca(b)
                i += 1
            elif len(fila) == 4:
                titulo = fila[0]
                autor = fila[1]
                numero = fila[2]
                genero = fila[3]
                # Diferencia entre composicion y agregacion
                l = Libro(titulo, autor, numero, genero)
                self.__listaB[i-1].agregarLibro(l)
        archivo.close()

    def funcion1(self):
        titulo = input("Ingrese el titulo del libro: \n")
        autor = input("Ingrese el autor del libro: \n")
        numero = input("Ingrese el numero del libro: \n")
        genero = input("Ingrese el genero del libro: \n")
        elec = int(input(
            "Biblioteca a insertar libro,Ingrese 0 para la CENTRAL o 1 para la POPULAR\n"))
        libro = Libro(titulo, autor, numero, genero)
        self.__listaB[elec].agregarLibro(libro)

    def funcion2(self):
        titulo = input("Ingrese el titulo del libro a eliminar: \n")
        for biblioteca in self.__listaB:
            for libro in biblioteca.getLibros():
                if libro.getTitulo() == titulo:
                    biblioteca.getLibros().remove(libro)
                    print(f"Libro '{titulo}' eliminado correctamente.")
                    return
        print(f"Libro '{titulo}' no encontrado.")

    def funcion3(self):
        titulo = input("Ingrese el titulo del libro a buscar: \n")
        for biblioteca in self.__listaB:
            for libro in biblioteca.getLibros():
                if libro.getTitulo() == titulo:
                    print(biblioteca)
                    return

    def funcion4(self):
        for biblioteca in self.__listaB:
            print(biblioteca)
            for libro in biblioteca.getLibros():
                print(libro)
