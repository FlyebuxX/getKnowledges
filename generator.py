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
        self.words_list = loadings.file_loading(self.words_list)
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
        obj.add_in_file(toWrite)

    def add_acquired_file_writing(self, toWrite):
        """
        Writing a piece of information in the acquired file
        :param toWrite: new to add
        """
        obj = methods.Method("acquiredWords.txt", self.path)
        obj.add_in_file(toWrite)

    def delete_in_progress_file(self, guessed_word):
        """
        Delete a piece of information from the in_progress_file
        :param guessed_word: acquired word
        """
        new_progress_list = [elt + "\n" for elt in self.in_progress_list if guessed_word not in elt]

        obj = methods.Method("inProgressWords.txt", self.path)
        obj.write_in_file(new_progress_list)


# ======================================================================================================================
# MAIN
# ======================================================================================================================


gen = Generator("english", "english")
gen.files()

