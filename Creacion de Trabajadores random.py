# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:25:17 2023

@author: Pedro
"""
#%%
import numpy as np
import clases as c
import random as rd
import view as v
#%%
contratos=np.arange(0,1,0.25)


#%%
def generate_random_worker_basic():
  contratos = np.arange(0, 1, 0.25)

  number_contract = rd.randint(1, np.size(contratos))

  contract_type = contratos[number_contract-1]

  Id = rd.randint(1, 10000)

  return c.Worker(Id, contract_type)


def generate_random_worker_complete():
  Id = rd.randint(1, 10000)

  contratos = np.arange(0.25, 1.25, 0.25)

  number_contract = rd.randint(2, np.size(contratos)+1)

  contract_type = contratos[number_contract-2]

  dias_trabajados = rd.randint(0, 4)

  findes_trabajados = rd.randint(0, 5)

  hours_worked = rd.randint(0, 1200)

  return c.Worker(Id, contract_type, findes_trabajados, dias_trabajados, hours_worked)


pepe = generate_random_worker_complete()
print(str(pepe.ID))
print(str(pepe.contract))
print(str(pepe.days_working_in_a_row))
print(str(pepe.weekend_counter))
print(str(pepe.hours_worked))
print(str(pepe.yearly_hours))


def generate_worker_to_CSV_list_format(pepe):
  list = []
  list.append(str(pepe.ID))
  list.append(str(pepe.contract))
  list.append(str(pepe.days_working_in_a_row))
  list.append(str(pepe.hours_worked))
  list.append(str(pepe.yearly_hours))
  return list

lista_pepe = generate_worker_to_CSV_list_format(pepe)
print(lista_pepe)
v.menu_manejo_turnos()