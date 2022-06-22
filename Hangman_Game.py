import random
import Functions


def play():
    Functions.header('Hangman Game')

    hit = False
    hanged = False
    play_game = True

    ######################################
    # Start the game
    ######################################

    while play_game:

        miss = 0

        secret_word = random_secret_word()

        word = ['_' for letter in secret_word]

        while not hit and not hanged:
            print(word)
            print('You have {} attempts'.format(miss))
            choose_letter = input('Choose a letter -> ')
            choose_letter = choose_letter.strip().upper()

            if choose_letter in secret_word:
                confirm_letter(secret_word, choose_letter, word)
            else:
                ######################
                # You lose
                ######################
                miss += 1
                drawing(miss)
                game_over = (miss == 7)

            ######################
            # You lose
            ######################
            if game_over:
                Functions.lose()
                break

            ######################
            # You win
            ######################
            win = "_" not in word
            if win:
                Functions.win()
                break

        ######################
        # Continue or not the while play_game
        ######################

        assistant = int(input('Do you want to continue playing? [0 for not | 1 for yes] '))
        if assistant == 1:
            play_game = True
        elif assistant == 0:
            play_game = False

    Functions.end_game()


def random_secret_word():
    ######################################
    # creating a vector word
    ######################################
    word = []

    with open('Secret_Words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            word.append(line)

    ######################################
    # Selecting a random word for the secret word
    ######################################

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()
    return secret_word


def confirm_letter(secret_word, choose_letter, word):
    index = 0
    for letter in secret_word:
        if letter == choose_letter:
            word[index] = choose_letter
        index = index + 1


def drawing(miss):
    print("  _______     ")
    print(" |/      |    ")

    if miss == 1:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if miss == 2:
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if miss == 3:
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if miss == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if miss == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if miss == 6:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if miss == 7:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if __name__ == "__main__":
    play()
