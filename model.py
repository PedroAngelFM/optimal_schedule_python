import clases as c
import pandas


class Model:
    def __init__(self):
        self.data_frame = pandas.DataFrame()

    # Primero se debe  intentar traer los datos desde una base de datos SQL y luego
    # ya intentar importarlo desde un CSV que lo traiga todo.
    def inicio_programa(self):
        self.importar_csv()
        print(self.data_frame.head())
        pass

    def importar_csv(self):
        self.data_frame = pandas.read_csv("base_datos.csv")
