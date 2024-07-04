# crie um codigo de jogo de par ou impar para jogar contra a maquina

from random import randint
cont = 0

while True:
    jogador = int(input("Informe um numero => "))
    pc = randint(0, 11)
    soma = jogador + pc 
    tipo = ' '
    while tipo not in "PI":
        tipo = str(input("PAR OU IMPAR [P/I] => ")).upper().strip()
    print("vc jogou {} e pc jogou {}".format(jogador, pc))
    if tipo == "P":
        if soma % 2 == 0: 
            print ("VOCE VENCEU!!")
            cont += 1
        else:
            print("VC PERDEU")
            break
    elif tipo == "I":
        if soma % 2 == 1:
            print("vc ganhou")
            cont += 1
        else:
            print("vc perdeu")
            break
    print("vamos jogar novamente...")
print("GANEM OVER. VC GANHOU  {} vezes".format(cont))        
