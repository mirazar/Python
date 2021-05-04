from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        day, month, year = [int(i) for i in data.split('-')]
        return f'{type(day)} {type(month)} {type(year)}'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Есть такая дата!'
        except ValueError:
            return 'Указана неправильная дата!'


print(Data.valid('29-35-2021'))
print(Data.type('29-35-21'))
