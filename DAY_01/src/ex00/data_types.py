def data_types():
    x1 = 1 #int
    x2 = "Hello, World!"
    x3= 2.2
    x4 = True
    x5 = ['s', 'p', ['isok'], 2]
    x6 = {1: 2, 2: 4, 3: 9}
    x7= (1, 1, 2, 2) #кортеж
    x8 = {'a', 'b', 'c', 'd'}

    print([type(x1).__name__, type(x2).__name__, type(x3).__name__, 
           type(x4).__name__, type(x5).__name__, type(x6).__name__, 
           type(x7).__name__, type(x8).__name__])


if __name__ == '__main__':
    data_types()


    #       > python3 data_types.py
    #   [int, str, float, bool, list, dict, tuple, set]