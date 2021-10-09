# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


from paths import Path
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

    def paths(self):
        """
        Paths function
        """
        new_path = Path()

        self.words_list = new_path.words_list()
        self.in_progress_list = new_path.in_progresss_list()
        self.acquired_words = new_path.acquired_words()
        self.foreign_words = new_path.foreign_words(self.lang)
        self.french_words = new_path.french_words()
