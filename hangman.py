import random

# FUNCTIONS!!! / Other stuff

stocks_pic = ["   ________      ",
              "           |     ",
              "           |     ",
              "           |     ",
              "           |     ",
              "           |     ",
              "           |     ",
              "           |     ",
              "================="]

for line in stocks_pic:
    print line


def hangman_single_guessing(hangman_answers, difficulty):
    print ""
    print "Hangman Time!"
    # This makes the _ _ _ _ _
    hangman_answer_array = []
    for i in range(0, len(hangman_answers)):
        hangman_answer_array.append("_")
    incorrect_letters = []
    # difficulty will be a number of which the number of tries left are based off of
    hangman_chances_left = int(difficulty)

    while "_" in hangman_answer_array and hangman_chances_left != 0:
        print hangman_answer_array
        """
        To cheat and check code
        print hangman_answers """

        letter_guess = raw_input("Guess a letter: ").upper()
        while letter_guess in hangman_answer_array or letter_guess in incorrect_letters or\
                (not letter_guess.isalpha() and letter_guess != " ") or len(letter_guess) != 1:
            if letter_guess in hangman_answer_array or letter_guess in incorrect_letters:
                print "You already guessed this letter!"
                letter_guess = raw_input("Guess a different letter!: ").upper()
            if not letter_guess.isalpha() and letter_guess != " " or len(letter_guess) != 1:
                letter_guess = raw_input("Guess one real letter of the English alphabet (e.g. A) or a space: ").upper()

        print ""

        if letter_guess in hangman_answers:
            print "You got one!"
            for i in range(0, len(hangman_answers)):
                if hangman_answers[i] == letter_guess:
                    hangman_answer_array[i] = letter_guess
                    # fix for multiple of same letter

        else:
            print "Nice try."
            incorrect_letters.append(letter_guess)
            incorrect_letters = sorted(incorrect_letters)
            hangman_chances_left -= 1
            # show stalks here
            if hangman_chances_left == 9:
                stocks_pic[1] = "  |        |     "
            elif hangman_chances_left == 8:
                stocks_pic[2] = ' [         |     '
            elif hangman_chances_left == 7:
                stocks_pic[2] = ' [ ]       |     '
            elif hangman_chances_left == 6:
                stocks_pic[2] = ' ["]       |     '
            elif hangman_chances_left == 5:
                stocks_pic[3] = '  |        |     '
                stocks_pic[4] = '  |        |     '
            elif hangman_chances_left == 4:
                stocks_pic[3] = ' /|        |     '
            elif hangman_chances_left == 3:
                stocks_pic[3] = ' /|\       |     '
            elif hangman_chances_left == 2:
                stocks_pic[5] = ' /         |     '
            elif hangman_chances_left == 1:
                stocks_pic[5] = ' / \       |     '
            elif hangman_chances_left == 0:
                stocks_pic[2] = '[XoX]      |     '
        print "Incorrect letters guessed: ", incorrect_letters
        print "Incorrect guesses left until you are hung: ", hangman_chances_left
        for elephant in stocks_pic:
            print elephant

    print hangman_answer_array

    if " " in hangman_answer_array:
        multiple_words = True
    else:
        multiple_words = False
    if "_" not in hangman_answer_array:
        if not multiple_words:
            print "Congrats! You guessed the word!"
        else:
            print "Congrats! You guessed the words!"
    else:
        print "You were close. The word was: ", hangman_answers


# Hangman begins


replay = True
while replay:
    print ""
    print "Welcome to Hangman!"

    stocks_pic = ["   ________      ",
                  "  |        |     ",
                  "           |     ",
                  "           |     ",
                  "           |     ",
                  "           |     ",
                  "           |     ",
                  "           |     ",
                  "================="]

    player_amount = raw_input(str("Single (1) or Multiplayer (2)?: "))
    while player_amount != "1" and player_amount != "2":
        player_amount = raw_input("You must type either 1 for Single or 2 for Multiplayer: ")
    print "You chose", player_amount
    print ""
    if player_amount == "1":
        print "The computer shall choose a word"
        print "All computer generated words only use characters from the alphabet (no spaces or punctuation)"
        print ""
        print "Chances left: 7"
        # Expert Wordlist
        dictionary2 = [
            "misnomer",
            "boolean",
            "coding",
            "accolade",
            "acrimony",
            "angst",
            "anomaly",
            "antidote",
            "baroque",
            "boondoggle",
            "bravado",
            "brogue",
            "brusque",
            "cacophony",
            "camaraderie",
            "capricious",
            "caustic",
            "charisma",
            "cloying",
            "dichotomy",
            "dilettante",
            "disheveled",
            "elan",
            "ennui",
            "epitome",
            "equanimity",
            "equivocate",
            "esoteric",
            "euphemism",
            "fastidious",
            "fiasco",
            "finagle",
            "glib",
            "gregarious",
            "harbinger",
            "hedonist",
            "heresy",
            "idiosyncratic",
            "idyllic",
            "indelicate",
            "infinitesimal",
            "insidious",
            "junket",
            "kitsch",
            "litany",
            "lurid",
            "malaise",
            "malinger",
            "mantra",
            "maudlin",
            "mercenary",
            "minimalist",
            "narcissist",
            "nirvana",
            "oblivion",
            "ogle",
            "ostentatious",
            "ostracize",
            "panacea",
            "peevish",
            "perfunctory",
            "philistine",
            "precocious",
            "propriety",
            "quintessential",
            "rhetoric",
            "scintillating",
            "stigma",
            "sycophant",
            "teetotaler",
            "tryst",
            "ubiquitous",
            "untenable",
            "vicarious",
            "zealous"
        ]

        hangman_answer2 = dictionary2[random.randint(0, len(dictionary2))]
        hangman_answer2 = hangman_answer2.upper()
        """Because I'm a cheater
        print hangman_answer2)"""

        hangman_single_guessing(hangman_answer2, 7)
    else:
        # Multiplayer
        print "Multiplayer"
        print ""
        hangman_answer = str(raw_input("The player who will write the word(s) may type it here: ")).upper()
        hangman_answer_checker = hangman_answer
        b = " "
        for char in b:
            hangman_answer_checker = hangman_answer_checker.replace(char, "")
        while not hangman_answer_checker.isalpha():
            print hangman_answer, "is not an acceptable word. Use only letters from the english alphabet and spaces."
            hangman_answer = raw_input("Choose another word(s): ").upper()
            hangman_answer_checker = hangman_answer
            space = " "
            for char in space:
                hangman_answer_checker = hangman_answer_checker.replace(char, "")

        assigned_difficulty = 0
        while assigned_difficulty < 7:
            assigned_difficulty = raw_input("How many incorrect guesses should the guessed be allowed (at least 7): ")
        hangman_single_guessing(hangman_answer, assigned_difficulty)
    print ""
    replay = raw_input("Want to play again? (YES (1) or NO (2)): ")
    while replay != "1" and replay != "2":
        replay = raw_input("Play again? YES (Type 1) or NO (Type 2) (only two options here): ")
    if replay == "1":
        replay = True
    else:
        replay = False
print "Good game! Let's play again sometime!"