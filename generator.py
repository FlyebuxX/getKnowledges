# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


from englishClass import English
from germanClass import German
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

        self.WORDS_LIST = open(self.path + "/words.txt")
        self.in_progress_list = open(self.path + "/inProgressWords.txt")
        self.acquired_words = open(self.path + "/acquiredWords.txt")
        self.french_words = open(self.path + "/frenchWords.txt")
        self.english_words = open(self.path + "/englishWords.txt")


