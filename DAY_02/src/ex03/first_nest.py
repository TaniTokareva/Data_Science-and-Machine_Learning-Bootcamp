#python3 first_nest.py data.csv
import sys

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
            head_fract = (head_count / all_count) * 100
            tail_fract = (tail_count / all_count) * 100
            return head_fract, tail_fract

if __name__ == '__main__':
    data = Research(sys.argv[1]).file_reader()  # Получаем данные
    print(data)
    calc = Research.Calculations()  # Создаем объект для расчетов
    head_count, tail_count = calc.counts(data)  # Получаем количество голов и хвостов
    head_fract, tail_fract = calc.fractions(head_count, tail_count)
    print(head_count, tail_count)
    print(head_fract, tail_fract)

