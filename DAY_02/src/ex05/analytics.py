#
import sys
from random import randint

class Research():
    def __init__(self, path):
        self.path = path
        
    def file_reader(self, has_header=True):        
        with open(self.path, 'r') as file:
            text = file.read()          
        
        lines = text.split('\n')
        
        if len(lines) < 2:
            raise Exception("Incorrect number of lines")
        
        header = lines[0].strip().split(',')
        
        if len(header) != 2 or header != ['head', 'tail']:
            raise Exception("Incorrect header of table")
        
        if has_header:
            index = 1  # Начнем с 1, если есть заголовок
        else:
            index = 0  # Если нет заголовка, начнем с 0

        data = []  # Место для хранения данных
        
        for line in lines[index:]:
            line = line.strip()
            if line:  # Проверим, не пуста ли строка
                values = line.split(',')
                if len(values) != 2 or values[0] not in ['0', '1'] or values[1] not in ['0', '1']:
                    raise Exception('Incorrect data')
                data.append([int(val) for val in values])  # Добавляем строку в данные
        return data
    
    class Calculations():
        def __init__(self, data):
            self.data = data # Данные передаются в конструктор

        def counts(self, data):
            head_count = 0
            tail_count = 0
            
            for row in data:
                if row[0] == 1:
                    head_count += 1
                if row[1] == 1:
                    tail_count += 1
        
            return head_count, tail_count
        
        def fractions(self, head_count, tail_count):
                all_count = head_count + tail_count
                if all_count == 0:
                    return 0,0
                head_fract = (head_count / all_count) * 100
                tail_fract = (tail_count / all_count) * 100
                return head_fract, tail_fract
    
    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)  # Инициализация родительского класса

        def predict_random(self, num_of_steps) :
            predictions = []
            for _ in range (num_of_steps):
                x = randint(0,1)
                prediction = [x, 1 - x]
                predictions.append(prediction)
            return predictions
# функция predict_last(), которая просто возвращает последний элемент данных из file_reader()
        def predict_last(self):
            return self.data[-1] if self.data else []
        def save_file(self, data, file_name, extension='txt'):
            with open(f'{file_name}.{extension}', 'w') as file: #????
                file.write(data)



