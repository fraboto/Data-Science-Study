import random
import os
from utils import file_utils as fu
from utils import os_utils as ou
from utils import draw_utils as du


DATA_FILE_DIR = '/home/fraboto/study/DataScience/InterPython/hangman/data.txt' 


class Hangman():

    def __init__(self) -> None:
        self.__words_file = fu.File(DATA_FILE_DIR)
        self.__word = self.__words_file.get_random_line()
        self.__tries = 7
        self.__word_letter_dict = self.__get_word_letter_dict()
        self.__guess_word = list('_' * len(self.__word))
        self.used_letters = []


    def __get_word_letter_dict(self):

        word_letter_dict = {} 

        for index, letter in enumerate(self.__word):
            if letter in word_letter_dict:
                word_letter_dict[letter].append(index)
            else:
                word_letter_dict[letter] = [index]

        return word_letter_dict


    def __check_letter(self, letter):

        letter_indexes = self.__word_letter_dict.get(letter)

        if letter_indexes is not None:

            for index in letter_indexes:
                self.__guess_word[index] = letter.upper()

        else:
            self.__tries -= 1


    def __is_word_complete(self):

        return not '_' in self.__guess_word


    @property
    def guess_word(self):
        return ' '.join(self.__guess_word)


    def play_again(self):

        play_again = input('\nWould you like to play again? [y/n]: ')

        if play_again.lower() == 'y':
            self.__reset_game()

        return play_again.lower() == 'y'


    def __reset_game(self):

        self.__word = self.__words_file.get_random_line()
        self.__tries = 7
        self.__word_letter_dict = self.__get_word_letter_dict()
        self.__guess_word = list('_' * len(self.__word))
        self.used_letters = []

        print('\n NEW GAME! \n')

        self.play_game()


    def play_game(self):

        self.__init_game()


    def __append_used_letter(self, letter):

        if not letter in self.used_letters:
            
            self.used_letters.append(letter)


    def __show_used_letters(self):

        if len(self.used_letters) > 0:
                
                print(f'\nYou have used these letters: {", ".join(self.used_letters)}')


    def __init_game(self):
        ou.clear_console()
        du.draw_hangman_word()
        du.draw_hangman(self.__tries)
        print(f'\n{self.guess_word}')

        while self.__tries > 0:

            self.__show_used_letters()

            try:
                guess_letter = input('\nInsert a letter: ').lower()

                ou.clear_console()
                du.draw_hangman_word()

                if len(guess_letter) != 1:
                    raise ValueError('\nYou have to enter one letter!')

                if not guess_letter.isalpha():
                    raise TypeError('\nYou have to enter a letter!')

            except (ValueError, TypeError) as e:
                self.__tries -= 1
                print(e)

            else:
                self.__append_used_letter(guess_letter.upper())
                self.__check_letter(guess_letter)

            finally:
                du.draw_hangman(self.__tries)
                print('\n', self.guess_word)
                if self.__is_word_complete():

                    du.draw_win()
                    return None

        du.draw_lost()
        print(f'\nThe word was: {self.__word}')
        return None


def run():
    hangman = Hangman()
    hangman.play_game()

    play = True

    while play:

        play = hangman.play_again()


if __name__ == '__main__':
    run()