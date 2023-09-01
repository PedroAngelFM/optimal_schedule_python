# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:25:17 2023

@author: Pedro
"""
import random as rd
# %%
import numpy as np
import clases as c
import pandas as pd

# %%
contract_types = np.arange(0, 1, 0.25)


# %%
def generate_random_worker_basic():
  contratos = np.arange(0, 1, 0.25)

  number_contract = rd.randint(1, np.size(contratos))

  contract_type = contratos[number_contract - 1]

  identifications = rd.randint(1, 10000)

  return c.Worker(identifications, contract_type)


def generate_random_worker_complete():
  identification = rd.randint(1, 10000)

  contract_types = np.arange(0.25, 1.25, 0.25)

  number_contract = rd.randint(2, np.size(contract_types) + 1)

  contract_type = contract_types[number_contract - 2]

  dias_trabajados = rd.randint(0, 4)

  findes_trabajados = rd.randint(0, 5)

  hours_worked = rd.randint(0, int(contract_type*1200))

  return c.Worker(identification, contract_type, findes_trabajados, dias_trabajados, hours_worked)


pepe = generate_random_worker_complete()
print(str(pepe.ID))
print(str(pepe.contract))
print(str(pepe.days_working_in_a_row))
print(str(pepe.weekend_counter))
print(str(pepe.hours_worked))
print(str(pepe.yearly_hours))


def generate_worker_to_CSV_list_format(pepe):
  list = []
  list.append(int(pepe.ID))
  list.append(float(pepe.contract))
  list.append(int(pepe.days_working_in_a_row))
  list.append(int(pepe.hours_worked))
  list.append(int(pepe.yearly_hours))
  return list


def generate_worker_as_dictionary(worker):
  worker_as_dictionary = {'ID': worker.ID, 'contract': worker.contract,
                          'days_working_in_a_row': worker.days_working_in_a_row, 'hours_worked': worker.hours_worked,
                          'yearly_hours': worker.yearly_hours}
  return worker_as_dictionary


lista_pepe = generate_worker_to_CSV_list_format(pepe)
print(lista_pepe)
data_frame_a_exportar = pd.DataFrame(
  columns=['ID', 'contract', 'days_working_in_a_row', 'hours_worked', 'yearly_hours'])
print(data_frame_a_exportar.columns)


def add_worker_to_dataframe(data_frame):
  worker = generate_random_worker_complete()
  new_worker_dict = generate_worker_as_dictionary(worker)
  data_frame.loc[len(data_frame)] = new_worker_dict


for i in range(100):
  add_worker_to_dataframe(data_frame_a_exportar)

print(data_frame_a_exportar.head(len(data_frame_a_exportar)))
