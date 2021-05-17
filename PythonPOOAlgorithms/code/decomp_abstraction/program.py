class Program:
    
    def __init__(self, name, needed_memory, needed_cpu):
        self._name = name
        self._needed_memory = needed_memory
        self._needed_cpu = needed_cpu

    def get_name(self):
        return self._name
    
    def get_needed_memory(self):
        return self._needed_memory
    
    def get_needed_cpu(self):
        return self._needed_cpu