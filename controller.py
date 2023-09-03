import model as md

m = md.Model()


class Control:
    def __init__(self):
        pass
    def inicio_programa(self):
        m.inicio_programa()
        pass

    def id_check(self, id_nuevo_trabajador):
        return m.id_check(id_nuevo_trabajador)
        pass

    def create_worker(self, id_nuevo_trabajador, tipo_contrato, weekend_counter, days_working_in_a_row,
                      hours_worked_in_a_year):
        m.create_worker(id_nuevo_trabajador, tipo_contrato, weekend_counter, days_working_in_a_row,
                      hours_worked_in_a_year)
        pass


