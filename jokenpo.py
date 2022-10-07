from random import randint
itens = ("Pedra", "papel", "Tesoura")
computador = randint(0,2)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Opções\n[0] Pedra\n[1] Papel\n[2] Tesoura")
user = int(input("Digite a sua escolha: "))
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("O user escolheu {}".format(itens[user]))
print("O computador escolheu {}".format(itens[computador]))

# condições
if user == computador:
    print("EMPATE!! Como assim?")
    #pedra resultados
elif computador == 0:
    if user == 1:
        print("Sim você GANHOOU!!")
    elif user == 2:
        print("Pelo jeito vc PERDEU!!")
    else:
        print("Jogada invalida!")

elif computador == 1:
    if user == 0:
        print("Pelo jeito vc PERDEU!!")
    elif user == 2:
        print("Sim você GANHOOU!!")
    else:
        print("Jogada invalida!")

elif computador == 2:
    if user == 1:
        print("Pelo jeito vc PERDEU!!")
    elif user == 0:
        print("Sim você GANHOOU!!")
    else:
        print("Jogada invalida!")






