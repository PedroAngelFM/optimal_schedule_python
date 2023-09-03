# Este documento es el archivo  de vista
import controller as ct
import getpass

c = ct.Control()


class View:
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
        print("Va a crear un nuevo turno")
        print()
        pass

    def modificacion_turno(self):
        pass

    def eliminar_turno(self):
        pass

    def crear_trabajador(self):
        print("Creación de nuevo trabajador")
        id_nuevo_trabajador = int(input("Introduzca el numero de identificación de su nuevo trabajador"))
        while(c.id_check(id_nuevo_trabajador)):
            print("El id de su trabajador ya existe, vuelva a introducir")
            id_nuevo_trabajador = int(input("Introduzca la identificación de nuevo: "))

        print("Ahora debe elegir entre uno de los siguientes tipos de contrato que tenga el trabajador:")

        print(""" 1. Jornada Completa: 1200h anuales.
                       \n 2. Jornada Reducida: 900h anuales.
                       \n 3. Media Jornada : 600h anuales.
                       \n 4. Jornada ultrarreducida: 300h anuales""")
        option = int(input("Introduzca su opción: "))
        options = [1, 2, 3, 4]
        while option not in options:
            print("Opción errónea, vuelva a probar.")
            option = int(input("Introduzca su opción: "))
        if option == 1:
            print("Elegiste la opción 1.")
            tipo_contrato= 1.
        elif option == 2:
            print("Elegiste la opción 2.")
            tipo_contrato= 0.75
        elif option == 3:
            print("Elegiste la opción 3.")
            tipo_contrato= 0.5
        elif option == 4 :
            print("Elegiste la opción 4.")
            tipo_contrato = 0.25

        print("El resto de datos del trabajador se iniciarán a 0 si este es nueva contratación, en caso contrario, se han de detallar el resto ")
        respuesta = input("¿Es el empleado una nueva contratación? S/N")
        while respuesta.lower() not in ['s','n']:
            respuesta= input("Opción no válida, repita. S/N")
        if respuesta.lower() == "s":
            weekend_counter = 0

            days_working_in_a_row = 0

            hours_worked_in_a_year = 0
        elif respuesta.lower() == 'n':
            weekend_counter = int(input("¿Cuántos fines de semana lleva trabajados desde el último que haya descansado?"))

            days_working_in_a_row = int(input("¿Cuántos días lleva trabajando de seguido?"))

            hours_worked_in_a_year = int(input("¿Cuántas horas lleva trabajando este año?"))

        c.create_worker(id_nuevo_trabajador, tipo_contrato, weekend_counter, days_working_in_a_row, hours_worked_in_a_year)


    def modificar_trabajador(self):
        pass

    def eliminar_trabajador(self):
        pass
