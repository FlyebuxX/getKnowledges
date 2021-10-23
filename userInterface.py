# ======================================================================================================================
# IMPORTS
# ======================================================================================================================


import generator
# ======================================================================================================================
# FUNCTIONS
# ======================================================================================================================


def main_interface():
    """
    Main interface
    :return language: language, str
    :return game_mode: game_mode, str
    """

    language = input(
        "Langue : Allemand (german) ou Anglais (english)"
    )

    if language.lower() != "german" and language.lower() != "english":

        while True:
            print("Merci de saisir un mode de jeu valide\n")
            language = input(
                "Langue : Allemand (german) ou Anglais (english)"
            )

            if language.lower() == "german" or language.lower() == "english":
                break

    game_mode = input("En langue " + language + " mode : " + language + " ou french")

    if game_mode.lower() != language and game_mode.lower() != "french":

        while True:
            print("Merci de saisir un mode de jeu valide\n")
            game_mode = input(
                "En langue " + language + " mode : " + language + " ou french"
            )

            if game_mode.lower() == "alld" or game_mode.lower() == "gb":
                break

    return language, game_mode


def translation(lang, word):
    """

    :param lang:
    :param word:
    :return:
    """
    if lang == "french":
        word_proposed = input("Quelle est la traduction de " + word[0] + "?")
        if word_proposed == word[1]:
            learning_status = True
            print("Correct ! La traduction de", word[0], "est bien", word[1])
        else:
            learning_status = False
            print("Faux ! La traduction de", word[0], "est", word[1], "et non pas", word_proposed)

        return word[0], learning_status

    else:
        word_proposed = input("Quelle est la traduction de " + word[1] + "?")
        if word_proposed == word[0]:
            learning_status = True
        else:
            learning_status = False
            print("Faux ! La traduction de", word[1], "est", word[0], "et non pas", word_proposed)
            print("Correct ! La traduction de", word[1], "est bien", word[0])

        return word[1], learning_status


def gen(lang, mode):
    """
    Generates a new object
    :param lang: str
    :param mode: str
    """
    obj = generator.Generator(lang, mode)
    obj.files()
    word_to_guess = obj.choose_word()

    TRANSLATE = translation(user_info[1], word_to_guess)
    obj.answers_counter(TRANSLATE[0], TRANSLATE[1])

    while True:
        play_again = input("\nSouhaitez vous continuer ? (y/n)")
        if play_again.lower() == "y":
            word_to_guess = obj.choose_word()
            TRANSLATE = translation(user_info[1], word_to_guess)
            obj.answers_counter(TRANSLATE[0], TRANSLATE[1])
        else:
            print("\nMerci d'avoir particpé, à bientôt !")
            break


# ======================================================================================================================
# MAIN
# ======================================================================================================================


user_info = main_interface()
gen(user_info[0], user_info[1])
