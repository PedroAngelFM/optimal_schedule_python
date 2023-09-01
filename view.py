# Este documento es el archivo  de vista
import controller as ct
import getpass

c = ct.control()


class vista:
    def __init__(self):
        pass

    def inicio_programa(self):
        print("Se iniciará el programa")

        print("Introduzca su usuario y contraseña para la base de datos")

        user = input("Usuario: ")

        #password = getpass.getpass("Contraseña: ")

        c.inicio_programa(user,"password")

    def menu_principal(self):
        print("============== Menú Principal ==============")
        print(""" 1. Menu Turnos.
               \n 2. Menú Trabajadores.
               \n 3. Menú Exportar/Importar. 
               \n 4. Salir""")
        option = int(input("\n Introduzca su opción: "))
        options = [1, 2, 3]
        while option not in options:
            print("Opción errónea, vuelva a probar.")
            option = int(input("Introduzca su opción: "))
        if option == 1:
            print("Elegiste la opción 1.")
            self.menu_manejo_turnos()
        elif option == 2:
            print("Elegiste la opción 2.")
            self.menu_manejo_trabajadores()
        elif option == 3:
            print("Elegiste la opción 3.")
            self.eliminar_turno()

    def menu_manejo_turnos(self):
        print("============== Menú Turnos ==============")
        print(""" 1. Crear nuevo turno.
               \n 2. Modificar un turno existente.
               \n 3. Eliminar un turno existente. \n""")
        option = int(input("\n Introduzca su opción: "))
        options = [1, 2, 3]
        while option not in options:
            print("Opción errónea, vuelva a probar.")
            option = int(input("Introduzca su opción: "))
        if option == 1:
            print("Elegiste la opción 1.")
            self.creacion_turno()
        elif option == 2:
            print("Elegiste la opción 2.")
            self.modificacion_turno()
        elif option == 3:
            print("Elegiste la opción 3.")
            self.eliminar_turno()

    def menu_manejo_trabajadores(self):
        print("============== Menú Trabajadores ==============")
        print(""" 1. Crear nuevo trabajador.
               \n 2. Modificar un trabajador existente.
               \n 3. Eliminar un trabajador existente. """)
        option = int(input("Introduzca su opción: "))
        options = [1, 2, 3]
        while option not in options:
            print("Opción errónea, vuelva a probar.")
            option = int(input("Introduzca su opción: "))
        if option == 1:
            print("Elegiste la opción 1.")
            self.crear_trabajador()
        elif option == 2:
            print("Elegiste la opción 2.")
            self.modificar_trabajador()
        elif option == 3:
            print("Elegiste la opción 3.")
            self.eliminar_trabajador()

    def creacion_turno(self):
        pass

    def modificacion_turno(self):
        pass

    def eliminar_turno(self):
        pass

    def crear_trabajador(self):
        pass

    def modificar_trabajador(self):
        pass

    def eliminar_trabajador(self):
        pass
