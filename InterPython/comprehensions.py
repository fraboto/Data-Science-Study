from math import sqrt

def run():
    
    #list comprehensions 
    even_squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(even_squares)

    four_six_nine_multiple = [ i for i in range(4, 100000, 4) if i % 18 == 0 ]
    print('múltiplos, con máximo 5 dígitos, del 4, 6 y 9: ', four_six_nine_multiple)

    #dictionary comprehensions
    cubes_dict = { key: key**3 for key in range(1, 101) if key % 3 != 0 }
    print('cubos de los primeros 100 dígitos', cubes_dict)

    square_roots = { i: sqrt(i) for i in range(1, 1001) }
    print('raíces de los primeros 1000 números naturales: ', square_roots)


if __name__ == '__main__':
    run()