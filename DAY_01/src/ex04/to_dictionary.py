def to_dictionary():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    
    dictionary = {}
    for country, number in list_of_tuples:
        if number in dictionary:
            dictionary[number].append(country)  # eсли ключ уже существует, добавляем страну в список
        else:
            dictionary[number] = [country]  # eсли ключа нет, создаем новый список с одной страной
    # print(dictionary)
    
    # вывод  словаря в требуемом формате
    for number, countries in dictionary.items():
        for country in countries:
            print(number, ':', country)


if __name__ == '__main__':
    to_dictionary()
