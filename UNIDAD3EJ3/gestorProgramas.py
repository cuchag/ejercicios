import csv
from Programa import Programa


class gestorProgramas:
    __programa: str

    def __init__(self):
        self.programas = []

    def agregar_programa(self, programa):
        self.programas.append(programa)

    def cargar_programas(self):
        archivo = open("programas.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            nombre = fila[0]
            codigo = fila[1]
            duracion = int(fila[2])
            p = Programa(nombre, codigo, duracion)
            self.agregar_programa(p)
        archivo.close()

    def buscar_programa_por_nombre(self, nombre):
        for programa in self.programas:
            if programa.get_nombre() == nombre:
                return programa
        return None
