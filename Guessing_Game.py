import random


def play():
    print(
        "      ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗ ")
    print(
        "      ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░  ██╔════╝░██╔══██╗████╗░████║██╔════╝ ")
    print(
        "      ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░ ")
    print(
        "      ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░ ")
    print(
        "      ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗ ")
    print(
        "      ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝ ")

    secret_number = random.randrange(1, 101)

    print("\n")

    attempts = 0
    multiplier = 1
    score = 1000

    level = int(input("Qual o nível de dificuldade ? [1|2|3|4|5]"))
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
        chute = int(input("Report your number [1-100]: "))

        if 1 > chute or chute > 100:
            print("Report a valid number between 1 and 100")
            continue

        hit = secret_number == chute
        higher = secret_number < chute
        lower = secret_number > chute

        if hit:
            print(' █▄█ █▀█ █░█   █░█░█ █ █▄░█')
            print(' ░█░ █▄█ █▄█   ▀▄▀▄▀ █ █░▀█')
            break
        else:
            pontos_perdidos = abs(secret_number - chute) * multiplier
            score = score - pontos_perdidos
            if lower:
                print("Your number was lower")
            elif higher:
                print("Your number was higher")

    print('Your score -> {} '.format(score))
    print('FIM DE JOGO')


if __name__ == "__main__":
    play()
