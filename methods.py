# ======================================================================================================================
# CLASS
# ======================================================================================================================


class Method:
    """
    Methods which manage with files
    """

    def __init__(self, file_name, path):
        self.file = file_name
        self.path = path

    def add_in_file(self, to_write):
        """
        Adding in a file
        :return:
        """
        file = open(self.path + "/" + self.file, "a", encoding="utf-8")
        file.write(to_write)
        file.close()

    def write_in_file(self, to_write):
        """
        Writing in a file
        :return:
        """
        file = open(self.path + "/" + self.file + "\n", "r", encoding="utf-8")
        file.write(to_write)
        file.close()
