# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


import paths
import loadings
import methods
import generator
# ======================================================================================================================
# FUNCTIONS
# ======================================================================================================================

def main_interface():
    """
    Main interface
    :return language: language choosen, str
    :return gamamode: gamemode choosen, str
    """

    language  = input(
        "Langue : Allemand (german) ou Anglais (english)"
    )

    if language.lower() != "alld" and language.lower() != "gb":

        while True:
            print("Merci de saisir un mode de jeu valide\n")
            language = input(
                "Langue : Allemand (german) ou Anglais (english)"
            )

            if language.lower() == "alld" or language.lower() == "gb":
                break

    gamemode = input("En langue " + language + " mode : " + language + " ou french")

    if gamemode.lower() != language and gamemode.lower() != "fr":

        while True:
            print("Merci de saisir un mode de jeu valide\n")
            gamemode = input(
                "En langue " + language + " mode : " + language + " ou french"
            )

            if gamemode.lower() == "alld" or gamemode.lower() == "gb":
                break

    return language, gamemode


def translation(lang, word):
    """

    :param lang:
    :param word:
    :return:
    """
    if lang == "french":
        word_proposed = input("Quelle est la traduction de " + word[0] + "?")
        if word_proposed == word[1]:
            learning_statut = True
            print("Correct ! La traduction de", word[0], "est bien", word[1])
        else:
            print("Faux ! La traduction de", word[0], "est", word[1], "et non pas", word)

        return word[0], learning_statut

    else:
        word_proposed = input("Quelle est la traduction de " + word[1] + "?")
        if word_proposed == word[0]:
            learning_statut = True
        else:
            print("Faux ! La traduction de", word[1], "est", word[0], "et non pas", word)
            print("Correct ! La traduction de", word[1], "est bien", word[0])

        return word[1], learning_statut


def generator(lang, mode):
    """
    Generates a new object
    :param lang: str
    :param mode: str
    """
    obj = generator.Generator(lang, mode)
    obj.files()
    word_to_guess = obj.choose_word()


# ======================================================================================================================
# MAIN
# ======================================================================================================================


user_info = main_interface()
generator(user_info[0], user_info[1])
