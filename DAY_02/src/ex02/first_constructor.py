#python3 first_constructor.py data.csv

import sys

class Research():
    def __init__(self, path):
        self.path = path
    def file_reader(self):        
        with open(self.path, 'r') as file:
            text = file.read()          
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            new_lines = [line  for line in lines if line != '']
            for i in range (1, len(set(new_lines))):
                if new_lines[i] != '1,0' and new_lines[i] != '0,1':
                    raise Exception('Incorrect line')
            if len(lines) < 2:
                raise Exception ("Incorrect number of lines")           
            header = line.split(',')
            if len(set(header)) != 2:
                raise Exception ("Incorrect header of table")
        
            return text
    

if __name__ == '__main__':
    x = Research(sys.argv[1])
    print(x.file_reader())
