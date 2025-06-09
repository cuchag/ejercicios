import csv
from Matricula import Matricula


class gestorMatricula:
    __matriculas: list

    def __init__(self):
        self.matriculas = []

    def agregar_matricula(self, matricula):
        self.matriculas.append(matricula)

    def cargar_matriculas(self, gestor_empleados, gestor_programas):
        archivo = open("matriculas.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)  # Skip the header row
        for fila in reader:
            fecha = fila[0]
            nombre_empleado = fila[1]
            nombre_programa = fila[2]

            # Find the corresponding Empleado and Programa objects
            empleado = gestor_empleados.buscar_empleado_por_nombre(
                nombre_empleado)
            programa = gestor_programas.buscar_programa_por_nombre(
                nombre_programa)

            if empleado is not None and programa is not None:
                matricula = Matricula(fecha, empleado, programa)
                self.agregar_matricula(matricula)
            else:
                print(
                    f"Error: No se encontró el empleado '{nombre_empleado}' o el programa '{nombre_programa}'.")
        archivo.close()

    def buscar_programa(self, programa):
        for matricula in self.matriculas:
            if matricula.get_nombre_programa() == programa:
                print(
                    f"Empleado: {matricula.get_nombre_empleado()}, Programa: {matricula.get_nombre_programa()}, Fecha: {matricula.get_fecha()}")
