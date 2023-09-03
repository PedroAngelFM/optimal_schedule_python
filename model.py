import clases as c
import pandas as pd


class Model:
  def __init__(self):
    self.data_frame_workers = pd.DataFrame()
    self.data_frame_work_shifts = pd.DataFrame()

# Primero se debe  intentar traer los datos desde una base de datos SQL y luego
# ya intentar importarlo desde un CSV que lo traiga toodo.

  def inicio_programa(self):
    self.importar_csv()

  def importar_csv(self):
    self.data_frame_workers = pd.read_csv("base_datos.csv")

    self.data_frame_work_shifts = pd.read_csv("base_datos_turnos.csv")

  def create_worker(self, id_nuevo_trabajador, tipo_contrato, weekend_counter, days_working_in_a_row,
                    hours_worked_in_a_year):
    new_worker = c.Worker(id_nuevo_trabajador, tipo_contrato, weekend_counter, days_working_in_a_row,
                          hours_worked_in_a_year)
    self.data_frame_workers.loc[len(self.data_frame_workers)] = new_worker.generate_worker_as_dictionary()

  def id_check(self, id_nuevo_trabajador):
    is_id_in_use = id_nuevo_trabajador in self.data_frame_workers['ID'].values
    return is_id_in_use
