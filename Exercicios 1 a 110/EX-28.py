# crie um codigo que VOCE tem que escolher um numero igual ao do PC ;)
import random
from time import sleep

pc = random.randint(0, 5)
num = int(input("Digite um numero de 0 a 5 => "))
print("PROCESSANDO...")
sleep (3)
print(f"VOCE ESCOLHER {num} o PC ESCOLHER {pc}")
if num == pc:
    print("voce venceu") 
else:
    print("VOCE PERDEU")
print("obrigada por jogar") 

# ou 

from random import randint

pc = randint(0, 5)
num = int(input("Digite um numero de 0 a 5 => "))
print(f"VOCE ESCOLHER {num} o PC ESCOLHER {pc}")
if num == pc:
    print("voce venceu") 
else:
    print("VOCE PERDEU")
print("obrigada por jogar")
