import random
import Functions


def play():

    Functions.header('Guessing Game')

    play_game = True
    while play_game:

        secret_number = random.randrange(1, 101)

        print("\n")

        attempts = 0
        multiplier = 1
        score = 1000

        level = int(input("What is the difficulty level ? [1|2|3|4|5]"))
        if level == 1:
            attempts = 12
            multiplier = 2
            score = 300
        elif level == 2:
            attempts = 10
            multiplier = 2.5
            score = 400
        elif level == 3:
            attempts = 8
            multiplier = 3
            score = 600
        elif level == 4:
            attempts = 5
            multiplier = 4
            score = 800
        elif level == 5:
            attempts = 3
            multiplier = 5
            score = 1000

        attempt_number = 1

        for attempt_number in range(1, attempts + 1):

            print("Attempt:{} of {}".format(attempt_number, attempts))
            number = int(input("Report your number [1-100]: "))

            if 1 > number or number > 100:
                print("Report a valid number between 1 and 100")
                continue

            hit = secret_number == number
            higher = secret_number < number
            lower = secret_number > number

            ######################
            # if you win
            ######################
            if hit:
                Functions.win()
                break
            else:
                lost_score = abs(secret_number - number) * multiplier
                score = score - lost_score
                if lower:
                    print("Your number was lower")
                elif higher:
                    print("Your number was higher")

        ######################
        # if you lose
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


if __name__ == "__main__":
    play()


