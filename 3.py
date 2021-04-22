class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        return full_name

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        return total_income


worker = Position('Иванов', 'Иван', 'менеджер', {'wage': 20000, 'bonus': 1000})
print(worker.get_full_name())
print(worker.position)
print(worker.get_total_income())
