# crie um codigo que o computador escolha entre 5 alunos para ser represetante (usar listas)
import random
aluno1 = str((input("Digite seu nome =>")))
aluno2 = str((input("Digite seu nome =>")))
aluno3 = str((input("Digite seu nome =>")))
aluno4 = str((input("Digite seu nome =>")))
aluno5 = str((input("Digite seu nome =>")))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
pc_escolhe = random.choice(lista)
print(f"O PC ESCOLHEU {pc_escolhe}")

# OU 

from random import choice

aluno1 = str((input("Digite seu nome =>")))
aluno2 = str((input("Digite seu nome =>")))
aluno3 = str((input("Digite seu nome =>")))
aluno4 = str((input("Digite seu nome =>")))
aluno5 = str((input("Digite seu nome =>")))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
pc_escolhe = choice(lista)
print(f"O PC ESCOLHEU {pc_escolhe}")



    

