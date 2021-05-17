def nombre_completo(nombre, apellido, reversar=False):
    if reversar:
        return f'{apellido} {nombre}'
    else:
        return f'{nombre} {apellido}'

print(nombre_completo('Ariel', reversar=True, apellido='Sirenita'))