# crie um codigo de papel, pedra e tesoura e jogue com a máquina

import random
pc_escolhe = random.randint(1, 3)
vc_escolhe = int(input("""[1] PEDRA
[2] PAPEL
[3] TESOURA """))
print("VC ESCOLHER {}".format(vc_escolhe))
print("o pc esoclher {}".format(pc_escolhe))

if pc_escolhe == 1:
    if vc_escolhe == 1:
        print("Empate")
    elif vc_escolhe == 2:
        print("Voce venceu")
    elif vc_escolhe == 3:
        print("PC VENCEU")
    else:
        print("opção invalida")
if pc_escolhe == 2:
    if vc_escolhe == 1:
        print("PC VENCEU")
    elif vc_escolhe == 2:
        print("Empate")
    elif vc_escolhe == 3:
        print("VC VENCEU")
    else:
        print("opção invalida")
if pc_escolhe == 3:
    if vc_escolhe == 1:
        print("PC VENCEU")
    elif vc_escolhe == 2:
        print("vc venceu")
    elif vc_escolhe == 3:
        print("Empate")
    else:
        print("opção invalida")

# OU 

import random
lista = ('PEDRA', 'PAPEL', 'TESOURA')
pc = random.randint(1, 3)
print('''ESCOLHA:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
resp = int(input('SUA OPÇÃO => '))
print('NFC JOGOU {}'.format(lista[pc]))
print('VOCÊ JOGOU {}'.format(lista[resp]))
if pc == 1: # NFC JOGOU PEDRA
    if resp == 1:
        print('EMPATE')
    elif resp == 2:
        print('VOCÊ VENCEU')
    elif resp == 3:
        print('NFC VENCEU')
    else:
        print('\033[31m JOGADA INVÁLIDA')
elif pc == 2: # NFC JOGOU PAPEL
    if resp == 1:
        print('NFC VENCEU')
    elif resp == 2:
        print('EMPATE')
    elif resp == 3:
        print('VOCÊ VENCEU')
    else:
        print('\033[31m JOGADA INVÁLIDA')
elif pc == 3: # NFC JOGOU TESOURA
    if resp == 1:
        print('VOCÊ VENCEU')
    elif resp == 2:
        print('NFC VENCEU')
    elif resp == 3:
        print('EMPATE')
    else:
        print('\033[31m JOGADA INVÁLIDA')