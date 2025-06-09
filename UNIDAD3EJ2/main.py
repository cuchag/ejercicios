from gestorBiblioteca import gestorBiblioteca


def menu():
    op = None
    try:
        op = int(input("""----MENU DE OPCIONES----
        1-Agregar Libro
        2-Eliminar Libro
        3-Busqueda por nombre de libro
        4-Lista de libros                      
        """))
    except ValueError:
        pass
    return op


if __name__ == "__main__":
    gestor = gestorBiblioteca()
    gestor.cargarDatos()
    op = menu()
    while op != 0:
        if op == 1:
            gestor.funcion1()
        elif op == 2:
            gestor.funcion2()
        elif op == 3:
            gestor.funcion3()
        elif op == 4:
            gestor.funcion4()
        else:
            print("Opcion no valida intente nuevamente")
        op = menu()
