# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


# ======================================================================================================================
# CLASS
# ======================================================================================================================


class Path:
    """
    Class which defines english propreties
    """

    def __init__(self, path):
        self.path = path

    def words_list(self):
        """
        Creating the wordsList
        :return: words_list, list
        """
        LIST = open(self.path + "/words.txt", "r", encoding="utf-8")
        words_list = LIST.readlines()
        LIST.close()

        return words_list

    def in_progress_list(self):
        """
        Creating the inProgressList
        :return: in_progress_list, list
        """
        LIST = open(self.path + "/inProgressWords.txt", "r", encoding="utf-8")
        in_progress_list = LIST.readlines()
        LIST.close()

        return in_progress_list

    def acquired_words(self):
        """
        Creating the acquiredWordsList
        :return: acquired_words, list
        """
        LIST = open(self.path + "/acquiredWords.txt", "r", encoding="utf-8")
        acquired_words = LIST.readlines()
        LIST.close()

        return acquired_words

    def foreign_words(self, lang):
        """
        Creating the foreignWords list
        :return: foreign_words, list
        """
        LIST = open(self.path + "/" + lang + "Words.txt", "r", encoding="utf-8")
        foreign_words = LIST.readlines()
        LIST.close()

        return foreign_words

    def french_words(self):
        """
        Creating the frenchWords list
        :param lang: str, language
        :return: french_words, list
        """
        LIST = open(self.path + "/frenchWords.txt", "r", encoding="utf-8")
        french_words = LIST.readlines()
        LIST.close()

        return french_words

