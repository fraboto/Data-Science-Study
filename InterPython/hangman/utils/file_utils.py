import random
import unidecode


class File():

    def __init__(self, path) -> None:
        self.path = path
        self.num_lines = 0
        self.__file_lines = []
        self.__load_file(self.path)
        self.__prev_index = -1


    def __load_file(self, path):

        with open(path, 'r', encoding='utf-8') as f:

            self.__file_lines = [unidecode.unidecode(line.strip().lower()) for line in f]

        self.num_lines = len(self.__file_lines)


    def get_random_line(self):

        try:
            random_index = random.randint(0, self.num_lines - 1)

            if self.__prev_index != random_index:

                self.__prev_index = random_index
                return self.__file_lines[random_index] 
                
            else:
                self.get_random_line(self)
        
        except ValueError:

            print('The file has not been loaded or does not contain any line')


if __name__ == '__main__':
    pass