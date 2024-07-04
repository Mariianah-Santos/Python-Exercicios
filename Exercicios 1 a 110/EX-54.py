# crie um codigo para cadastra no minimo 10 pessoas. Depois faça que o codigo mostre quantos sao maior de idade e quantos sao menores

from datetime import date
ano_atual = date.today().year
total_menorIdade = 0
total_maiorIdade = 0
for c in range(1, 4):
    nascimento = int(input("Informe seu ano de nascimento => "))
    idade = ano_atual - nascimento
    if idade >= 18:
        total_maiorIdade += 1
    else:
        total_menorIdade +=1 
print("Total de MIORES DE IDADE:{}".format(total_maiorIdade))
print("Total de MENRES de idade: {}".format(total_menorIdade))