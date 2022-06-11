import Guessing_Game
import Hangman


def library():
    print('     ░██████╗░░█████╗░███╗░░░███╗███████╗  ██╗░░░░░██╗██████╗░██████╗░░█████╗░██████╗░██╗░░░██╗')
    print('     ██╔════╝░██╔══██╗████╗░████║██╔════╝  ██║░░░░░██║██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝')
    print('     ██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░░░░██║██████╦╝██████╔╝███████║██████╔╝░╚████╔╝░')
    print('     ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░░░░██║██╔══██╗██╔══██╗██╔══██║██╔══██╗░░╚██╔╝░░')
    print('     ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ███████╗██║██████╦╝██║░░██║██║░░██║██║░░██║░░░██║░░░')
    print('     ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ╚══════╝╚═╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░')

    print('[1] Guessing Game')
    print('[2] Hangman')

    game = int(input('Whats game do you want to play -> '))

    guessing_game = (game == 1)
    hangman = (game == 2)

    if guessing_game:
        print('You want play Guessing Game ')
        Guessing_Game.play()
    elif hangman:
        print('You want play Hangman')
        Hangman.play()


if __name__ == "__main__":
    play()
