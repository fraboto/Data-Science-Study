from components import *

class Computer:

    def __init__(self, color):
        self.color = color
        self._ram = RAM(16)
        self._hd = HD('SSD', '512GB')
        self._cpu = CPU('AMD', 'Ryzen 7', '4000 Series')
        self._state = 'off'

    def turn_on(self):
        if self._state != 'on':
            self._state = 'on'
            self._ram.init_os()
            self._cpu.turn_on()
            print('Computador encendido')

    def turn_off(self):
        if self._state != 'off':
            self._state = 'off'
            self._ram.clean()
            self._cpu.turn_off()
            print('Computador apagado')

    def open_program(self, program):
        try:
            if self._state == 'on':
                self._ram.open_program(program)
                self._cpu.open_program(program)
                print(f'{program.get_name()} abierto')
            else:
                print('Computador apagado')
        except CPUException as e:
            self._ram.close_program(program)
            print(e)
        except RAMException as e:
            print(e)

    def close_program(self, program):
        if self._state == 'on':
            self._ram.close_program(program)
            self._cpu.close_program(program)
            print(f'{program.get_name()} cerrado')
        else:
            print('Computador apagado')

    def get_open_programs(self):
        print(f'Los programas abiertos son {self._ram.get_open_programs()}')
