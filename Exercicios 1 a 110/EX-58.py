# crie um codigo para jagr com o computador. Voce so ganha o jogo se acerta o numero que o PC jogou ;)
import random
num = 0
cont = 0
pc_escolhe = random.randint(1, 10)
while num != pc_escolhe: 
    num = int(input("Informe um numero => "))
    cont += 1
    if num == pc_escolhe:
        print("Voce venceu")
    else:
        print("Vc perdeu")
        print("tente novamente")
        
print('NUMERO ESCOLHIDO PELO JOGADOR \033[31m{} \033[mE FORAM \033[34m{} \033[mTENTATIVAS'.format(num, cont))
print('NUMERO ESCOLHIDO PELO COMPUTADOR \033[37m{}'.format(pc_escolhe))