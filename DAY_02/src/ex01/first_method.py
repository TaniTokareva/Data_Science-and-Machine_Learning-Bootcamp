class Research:
    def file_reader(self):
        with open('data.csv', 'r') as file:
            text = file.read()
            return text
        

if __name__ == '__main__':
    x = Research()
    print(x.file_reader())
