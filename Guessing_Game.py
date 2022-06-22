import random
import Functions


def play():

    number = 0

    Functions.header('Guessing Game')

    play_game = True
    while play_game:

        secret_number = random.randrange(1, 101)

        print("\n")

        attempts = 0
        multiplier_score = 1
        score = 1000

        #######################
        # Declaring the level
        #######################
        level = int(input("What is the difficulty level ? [1|2|3|4|5]"))
        setting_level(level)

        attempt_number = 1

        for attempt_number in range(1, attempts + 1):

            #######################
            # Getting and setting the number
            #######################
            print("Attempt:{} of {}".format(attempt_number, attempts))
            number = int(input("Report your number [1-100]: "))

            if 1 > number or number > 100:
                print("Report a valid number between 1 and 100")
                continue

            hit = secret_number == number
            higher = secret_number < number
            lower = secret_number > number

            ######################
            # You win
            ######################
            if hit:
                Functions.win()
                break
            else:

                ######################
                # Scores Discount Systems
                ######################
                lost_score = abs(secret_number - number) * multiplier_score
                score = score - lost_score
                if lower:
                    print("Your number was lower")
                elif higher:
                    print("Your number was higher")

        ######################
        # You lose
        ######################
        if number != secret_number:
            Functions.lose()

        print('Your score -> {} '.format(score))

        assistant = int(input('Do you want to continue playing? [0 for not | 1 for yes] '))
        if assistant == 1:
            play_game = True
        elif assistant == 0:
            play_game = False

    Functions.end_game()


def setting_level(level):
    if level == 1:
        attempts = 12
        multiplier = 1
        score = 300
        return attempts, multiplier, score
    elif level == 2:
        attempts = 10
        multiplier = 2
        score = 400
        return attempts, multiplier, score
    elif level == 3:
        attempts = 8
        multiplier = 3
        score = 600
        return attempts, multiplier, score
    elif level == 4:
        attempts = 5
        multiplier = 4
        score = 800
        return attempts, multiplier, score
    elif level == 5:
        attempts = 3
        multiplier = 5
        score = 1000
        return attempts, multiplier, score


if __name__ == "__main__":
    play()


