def divisors(num):

    try:

        if num < 1:
            raise ValueError('¡ERROR! El número debe ser positivo')
        
        if type(num) is not int:
            raise TypeError('¡ERROR! El número debe ser un entero')

    except ValueError as ve:

        print(ve)
    
    except TypeError as te:

        print(te)

    else:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        return divisors


def run():
    try:

        num = int(input('Ingresa un número: '))
        num_divisors = divisors(num)
        if num_divisors != None:
            print(num_divisors)

    except ValueError as ve:

        print('¡ERROR! Debe ingresar un número')

    finally:
        print('El programa terminó')


if __name__ == '__main__':
    run()