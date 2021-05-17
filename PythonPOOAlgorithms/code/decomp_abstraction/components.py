from exceptions import * 

class RAM:

    def __init__(self, capacity):
        self._capacity = capacity
        self._used = 0
        self._open_programs = []

    def init_os(self):
        self._used = 4

    def open_program(self, program):
        if self._used + program.get_needed_memory() < self._capacity:
            self._open_programs.append(program.get_name())
            self._used += program.get_needed_memory()
        else:
            raise RAMException("¡RAM al máximo! No se pudo abrir el programa")

    def close_program(self, program):
        self._open_programs.remove(program.get_name())
        self._used -= program.get_needed_memory()

    def clean(self):
        self._used = 0
        self._open_programs = []

    def get_open_programs(self):
        return self._open_programs


class HD:

    def __init__(self, type, capacity):
        self._type = type
        self._capacity = capacity


class CPU:

    def __init__(self, brand, model, generation):
        self._brand = brand
        self._model = model
        self._generation = generation
        self._used_percentage = 0
        self._max_cpu = 100

    def turn_on(self):
        self.state = 'on'   
        self._used_percentage = 30

    def turn_off(self):
        self.state = 'off'
        self._used_percentage = 0

    def open_program(self, program):
        if self._used_percentage + program.get_needed_cpu() < self._max_cpu:
            self._used_percentage += program.get_needed_cpu()
        else:
            raise CPUException("¡CPU al máximo! No se pudo abrir el programa")

    def close_program(self, program):
        self._used_percentage -= program.get_needed_cpu()
