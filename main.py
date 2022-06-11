
print("        ░██████╗░██╗░░░██╗███████╗░██████╗░██████╗██╗███╗░░██╗░██████╗░  ░██████╗░░█████╗░███╗░░░███╗███████╗ ")
print("        ██╔════╝░██║░░░██║██╔════╝██╔════╝██╔════╝██║████╗░██║██╔════╝░  ██╔════╝░██╔══██╗████╗░████║██╔════╝ ")
print("        ██║░░██╗░██║░░░██║█████╗░░╚█████╗░╚█████╗░██║██╔██╗██║██║░░██╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░ ")
print("        ██║░░╚██╗██║░░░██║██╔══╝░░░╚═══██╗░╚═══██╗██║██║╚████║██║░░╚██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░ ")
print("        ╚██████╔╝╚██████╔╝███████╗██████╔╝██████╔╝██║██║░╚███║╚██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗ ")
print("        ░╚═════╝░░╚═════╝░╚══════╝╚═════╝░╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝ ")

numero_secreto = 26

print("\n")

tentativas = 0

level = input("Qual o nível de dificuldade ? [1|2|3|4|5]")
if level =='1':
    tentativas = 12
elif level =='2':
    tentativas = 10
elif level =='3':
    tentativas = 8
elif level =='4':
    tentativas = 5
elif level =='5':
    tentativas = 3

contador = 0


for contador in range(1, tentativas):

    print("Tentativa:{} de {}".format(contador, tentativas))
    chute_str = input("Informe o seu chute: ")

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if acertou:
        print("VOCÊ ACERTOU O NÚMERO")
        break
    else:
        if menor:
            print("Seu chute foi menor")
        elif maior:
            print("Seu chute foi maior")



