# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 09:27:37 2023

@author: Pedro Ángel Fraile Manzano 
"""


class Worker:

    # Un trabajador tiene los siguientes

    def __init__(self, ID, contract):
        self.ID = ID

        self.contract = contract

        self.weekend_counter = 0

        self.days_working_in_a_row = 0

        self.hours_worked = 0

        self.yearly_hours = 0

    def __init__(self, ID, contract, weekends, days_working_in_a_row, hours_worked_in_a_year):
        self.ID = ID

        self.contract = contract

        self.weekend_counter = weekends

        self.days_working_in_a_row = days_working_in_a_row

        self.hours_worked = hours_worked_in_a_year

        self.yearly_hours = self.contract * 1200

    def __str__(self):
        return """El trabajador tiene un ID"""

    def generate_worker_as_dictionary(self):
        worker_as_dictionary = {'ID': self.ID, 'contract': self.contract,
                                'days_warking_in_a_row': self.days_working_in_a_row,
                                'hours_worked': self.hours_worked, 'yearly_hours': self.yearly_hours}
        return dict

class Tipo_turno:
    def __init__(self, name, hours, night, weekend):
        self.name = name

        self.hours = hours

        self.night = night

        self.weekend = weekend
