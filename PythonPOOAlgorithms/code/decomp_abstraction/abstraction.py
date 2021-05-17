from computer import Computer
from program import *

if __name__ == '__main__':
    pc = Computer('azul')
    chrome = Program('Google Chrome', 1, 10)

    pc.turn_on()
    pc.open_program(chrome)
    pc.get_open_programs()
