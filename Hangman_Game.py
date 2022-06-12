import random
import Functions


def play():

    Functions.header('Hangman Game')

    word = []

    ######################################
    # Ope the file and close automatically
    ######################################
    with open('Secret_Words.txt', 'r') as file:
        for line in file:
            line = line.strip()
            word.append(line)

    ######################################
    # Selecting a random word for the secret word
    ######################################

    number = random.randrange(0, len(word))
    secret_word = word[number].upper()

    word = ['_' for letter in secret_word]

    hit = False
    hanged = False
    play_game = True
    miss = 6

    ######################################
    # Start the game
    ######################################

    while play_game:
        while not hit and not hanged:
            print(word)
            print('You have {} attempts'.format(miss))
            choose_letter = input('Choose a letter -> ')
            choose_letter = choose_letter.strip().upper()

            if choose_letter in secret_word:
                index = 0
                for letter in secret_word:
                    if letter == choose_letter:
                        print('You hit the letter')
                        word[index] = choose_letter
                    index = index + 1

            else:
                miss = miss - 1
                ######################
                # if you lose
                ######################
                game_over = (miss == 0)
                if game_over:
                    Functions.lose()
                    break

            ######################
            # if you win
            ######################
            win = "_" not in word
            if win:
                Functions.win()
                break
        assistant = int(input('Do you want to continue playing? [0 for not | 1 for yes] '))
        if assistant == 1:
            play_game = True
        elif assistant == 0:
            play_game = False

    Functions.end_game()


if __name__ == "__main__":
    play()
