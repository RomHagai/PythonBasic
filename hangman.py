import string


def print_start():
    """
    print the start string
    :return:
    """
    HANGMAN_ASCII_ART = """Welcome to the game Hangman
         | |  | |                                        
         | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
         |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
         | |  | | (_| | | | | (_| | | | | | | (_| | | | |
         |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                              __/ |                      
                             |___/
    """
    MAX_TRIES = 6

    print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES) + "\n")


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    check if valid
    :param letter_guessed: the guessed letter
    :param old_letters_guessed: list of old guessed letters
    :return: if the input letter is valid
    """
    return not (len(letter_guessed) > 1 or not (letter_guessed.lower() in string.ascii_letters) or (
            letter_guessed.lower() in old_letters_guessed))


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    try to add the letter to the list of old guessed letters
    :param letter_guessed: the guessed letter
    :param old_letters_guessed: list of old guessed letters
    :return: if the update succeeded
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed.lower())
        return True
    print("X")
    old_str = ""
    for i in old_letters_guessed:
        old_str = old_str + i + " -> "
    print(old_str[:-3])
    return False


def show_hidden_word(secret_word, old_letters_guessed):
    """
    create a new word
    :param secret_word: the secret word
    :param old_letters_guessed: list of old guessed letters
    :return:the new word
    """
    new_str = " "
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            new_str = new_str + secret_word[i] + " "
        else:
            new_str = new_str + " _ "
    return new_str


def check_win(secret_word, old_letters_guessed):
    """
    check if the player won
    :param secret_word:
    :param old_letters_guessed:
    :return:
    """
    new_str = show_hidden_word(secret_word, old_letters_guessed)
    ch = '_'
    return not (ch in new_str)


def print_hangman(num_of_tries):
    """
    print the status is the hangman
    :param num_of_tries:
    :return:
    """
    HANGMAN_PHOTHOS = {
        1: """
        x-------x
        """,
        2: """
        x-------x
        |
        |
        |
        |
        |
        """,
        3: """
        x-------x
        |       |
        |       0
        |
        |
        |
        """,
        4: """  
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,

        5: """
        x-------x
        |       |
        |       0
        |      /|\\
        |
        |
        """,
        6: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        |
      """,
        7: """
        x-------x
        |       |
        |       0
        |      /|\\
        |      / \\
        |
        """
    }
    print(HANGMAN_PHOTHOS[num_of_tries])


def choose_word(file_path, index):
    """
    extract word from the file
    :param file_path:
    :param index:
    :return:
    """
    input_file = open(file_path, "r")
    text = input_file.read()
    word_list = list(text.split(" "))
    while "" in word_list:
        word_list.remove("")

    # handle with duplicate words
    unique_words = []
    for word in word_list:
        if word not in unique_words and word != "":
            unique_words.append(word)

    while index > len(word_list):
        index = index - len(word_list)
    input_file.close()
    return word_list[index - 1]


def hangman(secret_word):
    """
    the final game
    :param secret_word:
    :return:
    """
    number_of_miss = 1
    MAX_MISS = 7
    print_hangman(number_of_miss)
    old_letters = []
    print(show_hidden_word(secret_word, old_letters))

    while number_of_miss < MAX_MISS and not (check_win(secret_word, old_letters)):
        letter = input("Please guess a letter: ")
        while not (try_update_letter_guessed(letter, old_letters)):
            letter = input("Please guess a letter: ")
            print("again")
        print(show_hidden_word(secret_word, old_letters))
        if letter.lower() not in secret_word:
            number_of_miss = number_of_miss + 1
            print_hangman(number_of_miss)
            print("You have only ", MAX_MISS - number_of_miss, " tries left")

    if check_win(secret_word, old_letters):
        print("YOU WON!")
    else:
        print("YOU LOST!")


def main():
    print_start()
    file_path = input("Please enter the file path: ")
    index = int(input("Please enter the index of the wanted word: "))
    secret_word = choose_word(file_path, index)
    hangman(secret_word)


if __name__ == '__main__':
    main()