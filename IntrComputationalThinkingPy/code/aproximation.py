import sys

objective = int(input('Escoge un número: '))

if objective < 0:
    sys.exit('No se puede encontrar la raíz cuadrada de números negativos')

epsilon = 0.01
step = epsilon**2
response = 0.0

while abs(response**2 - objective) >= epsilon:
    response += step

if abs(response**2 - objective) <= epsilon:
    print(f'La raíz de {objective} es {response}')
else:
    print(f'No se encontró la raíz de {objective}')