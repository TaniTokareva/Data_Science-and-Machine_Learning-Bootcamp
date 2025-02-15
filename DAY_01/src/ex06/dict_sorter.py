#Напишите программу, которая отображает названия стран в порядке убывания по номерам,
#а затем в алфавитном порядке по названиям, если номера совпадают. Вам нужно отображать
#по одному в строке, без цифр


def dict_sorter():
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
    
    # Преобразуем список кортежей в словарь
    country_dict = {country: int(number) for country, number in list_of_tuples}

    # Сортируем словарь по значениям (числам), затем по ключам (странам)
    sorted_countries = sorted(country_dict.items(), key=lambda item: (-item[1], item[0]))

    # Выводим только страны в отсортированном порядке
    for country, _ in sorted_countries:
        print(country)

if __name__ == '__main__':
    dict_sorter()
