objective = float(input('Escoge un número: '))

if objective < 0:
    sys.exit('No se puede encontrar la raíz cuadrada de números negativos')

epsilon = 0.00001
minimum = 0.0
maximum = max(objective, 1.0)
response = (maximum + minimum) / 2

while abs(response**2 - objective) >= epsilon:
    if response**2 < objective:
        minimum = response
    else:
        maximum = response
    response = (maximum + minimum) / 2

print(f'La raíz cuadrada de {objective} es {response}')