# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


from generator import Generator
from paths import Path
# ======================================================================================================================
# CLASS
# ======================================================================================================================


class Method:
    """
    Methods which can useful to deal with files
    """

    def __init__(self, file_name):
        self.file = file_name

    def open_file(self):
        """
        Opening file
        :return file:
        """
        file = open(self.file, "r", encoding="utf-8")
        return file

    def read_file(self):
        """
        Reading file
        :return file:
        """
        file = self.file.readlines()
        return file

    def close_file(self):
        """
        Closing file
        :return file:
        """
        file = self.file.close()
        return file