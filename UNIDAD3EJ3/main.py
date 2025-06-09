from gestorEmpleados import gestorEmpleados
from gestorMatricula import gestorMatricula
from gestorProgramas import gestorProgramas


def menu():
    op = None
    op = int(input("""----Elija la accion----
    
    1-Informe de duracion de programas a traves de id de empleado
    2-Lista de empleados inscriptos en programa
    3-Lista de empleados sin ningun programa
    """))
    return op


if __name__ == "__main__":
    gestorE = gestorEmpleados()
    gestorM = gestorMatricula()
    gestorP = gestorProgramas()
    gestorE.cargar_empleados()
    gestorP.cargar_programas()
    gestorM.cargar_matriculas(gestorE, gestorP)
    op = menu()
    while op != 0:
        if op == 1:
            id = int(input("Ingrese el id del empleado a buscar:\n"))
            gestorE.buscar_empleado(id, gestorM)
        elif op == 2:
            programa = input(
                "Ingrese programa a buscar respetar mayusculas y minusculas:\n")
            gestorM.buscar_programa(programa)
        elif op == 3:
            print("Listado de empleados sin ningun programa:")
            gestorE.buscavagos(gestorM)

        else:
            print("Opcion no valida, intente nuevamente")
        menu()
