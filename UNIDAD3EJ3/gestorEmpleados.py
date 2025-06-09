import csv
from Empleados import Empleado


class gestorEmpleados:
    __empleados = list

    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def cargar_empleados(self):
        archivo = open("empleados.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            try:
                nombre = fila[0]
                id = int(fila[1])
                puesto = fila[2]
                empleado = Empleado(nombre, id, puesto)
                self.agregar_empleado(empleado)
            except (ValueError, IndexError) as e:
                print(f"Error processing row {fila}: {e}")
                continue
        archivo.close()

    def buscar_empleado_por_nombre(self, nombre):
        for empleado in self.empleados:
            if empleado.getNombre() == nombre:
                return empleado
        return None

    def buscar_empleado(self, id, gestorM):
        for empleado in self.empleados:
            if empleado.getId() == id:
                nombre = empleado.getNombre()
                for matricula in gestorM.matriculas:
                    if matricula.get_nombre_empleado() == nombre:
                        print(
                            f"Empleado encontrado: {nombre},programa tomado:{matricula.get_programa()}")
        return None

    def buscavagos(self, gestorM):
        for empleado in self.empleados:
            if not any(matricula.get_nombre_empleado() == empleado.getNombre() for matricula in gestorM.matriculas):
                print(
                    f"Empleado que no registro ningun programa: {empleado.getNombre()}\n")
