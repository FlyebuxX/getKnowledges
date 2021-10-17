# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


import paths

# ======================================================================================================================
# FUNCTIONS
# ======================================================================================================================


def words_list_file_loading(file):
    """
    Load the words list file
    :param file: list
    :return tab: list of tuples
    """
    tab = []
    for elt in range(1, len(file)):  # excepting line 1 : languages used
        element = file[elt][:-1]  # deleting \n
        element = element.split(":")
        tab.append((element[0], element[1]))

    return tab


def file_loading(file):
    """
    Load a file
    :param file: list
    :return: list
    """
    tab = [file[elt][:-1] for elt in range(len(file))]

    return tab
