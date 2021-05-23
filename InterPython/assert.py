def get_name_from_letter(letter):
    '''
    La función get_name_from_letter recibe los parámetros a y b y retorna un nombre.
    En caso de recibir otra letra retorna NN.
    Puede suceder que otro código consuma esta función y esperando que c retorne un nombre se encuentre con que retorna NN.
    Esto se da porque puede que asumamos que letter puede tener el valor de 'c'. Lo cual es una asunción errada.
    Para resolver esto ver la función get_name_from_letter_assert
    '''
    if letter == 'a':
        return 'Antonio'
    elif letter == 'b':
        return 'Bonifacio'
    else:
        return 'NN'


def get_name_from_letter_assert(letter):
    '''
    La función get_name_from_letter_assert verifica que la entrada a esta función sea a, b, o una cadena vacía, de lo contrario genera un AssertionError. 
    Si otro código usa esta función esperando que, por ejemplo, 'c' le genere una salida, se encontrará que la función generará la excepción.
    Esto genera que si realmente se necesita que esta función retorne algo para la entrada 'c', 
    entonces se sabrá inmediatamente cuál es el error y permita realizar el cambio necesario.
    '''
    assert letter in ('a', 'b', ''), 'letter solo puede ser a, b, o cadena vacía'

    if letter == 'a':
        return 'Antonio'
    elif letter == 'b':
        return 'Bonifacio'
    else:
        return 'NN'


def run():
    
    letter = input('ingresa una letra: ')
    print('salida de get_name_from_letter: ', get_name_from_letter(letter[0] if len(letter) > 0 else ''))
    print('salida de get_name_from_letter_assert: ', get_name_from_letter_assert(letter[0] if len(letter) > 0 else ''))


if __name__ == '__main__':
    run()