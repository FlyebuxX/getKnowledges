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

    def __init__(self, file_name, path):
        self.file = file_name
        self.path = path

    def add_in_file(self, toWrite):
        """
        Adding in a file
        :return:
        """
        file = open(self.path + "/" + self.file, "a", encoding="utf-8")
        file.write(toWrite)
        file.close()

    def write_in_file(self, toWrite):
        """
        Writing in a file
        :return:
        """
        file = open(self.path + "/" + self.file + "\n", "r", encoding="utf-8")
        file.write(toWrite)
        file.close()