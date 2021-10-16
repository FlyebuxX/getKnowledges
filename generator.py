# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


import paths
import loadings
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


# ======================================================================================================================
# MAIN
# ======================================================================================================================


gen = Generator("english", "english")
gen.files()

