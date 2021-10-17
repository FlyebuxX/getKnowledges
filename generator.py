# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


import paths
import loadings
import methods
import random
# ======================================================================================================================
# CLASS
# ======================================================================================================================


class Generator:
    """
    Class which defines a generator
    """

    def __init__(self, language, gamemode):
        self.lang = language
        self.gamemode = gamemode
        self.path = language + "Package"

        new_path = paths.Path(self.path)

        self.words_list = new_path.words_list()
        self.in_progress_list = new_path.in_progress_list()
        self.acquired_words = new_path.acquired_words()
        self.foreign_words = new_path.foreign_words(self.lang)
        self.french_words = new_path.french_words()

    def files(self):
        """
        """
        self.words_list = loadings.words_list_file_loading(self.words_list)
        self.in_progress_list = loadings.file_loading(self.in_progress_list)
        self.acquired_words = loadings.file_loading(self.acquired_words)
        self.foreign_words = loadings.file_loading(self.foreign_words)
        self.french_words = loadings.file_loading(self.french_words)

    def choose_word(self):
        """
        Generates the word to guess
        :return duo: tuple
        """
        while True:

            word_to_guess = random.choice(self.words_list)

            if word_to_guess[0] not in self.acquired_words and self.gamemode == "french":  # if gamemode is french and the word is not acquired
                break
            elif word_to_guess[1] not in self.acquired_words and self.gamemode != "french":  # if gamemode is foreign and the word is not acquired
                break

        return word_to_guess

    def add_in_progress_file_writing(self, toWrite):
        """
        Writing a piece of information in the in_progress file
        :param toWrite: new to add
        """
        obj = methods.Method("inProgressWords.txt", self.path)
        obj.add_in_file(toWrite + "\n")

    def add_acquired_file_writing(self, toWrite):
        """
        Writing a piece of information in the acquired file
        :param toWrite: new to add
        """
        obj = methods.Method("acquiredWords.txt", self.path)
        obj.add_in_file(toWrite + "\n")

    def delete_in_progress_file(self, guessed_word):
        """
        Delete a piece of information from the in_progress_file
        :param guessed_word: acquired word
        """
        new_progress_list = [elt + "\n" for elt in self.in_progress_list if guessed_word not in elt]

        obj = methods.Method("inProgressWords.txt", self.path)
        obj.write_in_file(new_progress_list)

        return new_progress_list

    def answers_counter(self, word_to_guess, learning_statut):
        """
        Count right / wrong answers
        :param word_to_guess: word to guess, str
        :param learning_statut: bool
        """
        in_progress_words = [elt.split(" ")[0] for elt in self.in_progress_list ]
        in_progress_count = [elt.split(" ")[-1] for elt in self.in_progress_list]

        if word_to_guess in in_progress_words:  # if the word has already been proposed
            index = in_progress_words.index(word_to_guess)

            if learning_statut:  # if the translation is correct
                in_progress_count[index] = str(int(in_progress_count[index]) + 1)

                if int(in_progress_count[index]) == 10:
                    self.add_acquired_file_writing(word_to_guess)
                    self.delete_in_progress_file(word_to_guess)

                else:
                    self.add_in_progress_file_writing(in_progress_words[index] + " " + in_progress_count[index])

            else:
                in_progress_count[index] = str(int(in_progress_count[index][1]) - 1)
                self.add_in_progress_file_writing(in_progress_words[index] + " " + in_progress_count[index])

            print("(" + str(int(in_progress_count[index])) + " / 10)")


        else:  # if the word is proposed for the first time
            if learning_statut:
                new_word = word_to_guess + " " + "1"
                print("(1 / 10)")
            else:
                new_word = word_to_guess + " " + "-1"
                print("(-1 / 10)")
            self.add_in_progress_file_writing(new_word)


# ======================================================================================================================
# MAIN
# ======================================================================================================================


gen = Generator("english", "english")
gen.files()

