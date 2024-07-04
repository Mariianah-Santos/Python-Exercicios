# crie um codigo de cadastro de pessoas. Pergunte o sexo e a idade 
# mostre na tela, quantas pessoas se cadastraram com mas de 18. Mostra os homens que foram cadastrados. Mostra quantas mulheres com menos de 20 anos

 
resposta = "Ss"
idade = 0
sexo = 0
homens_cadastrado = 0
mulher_menos20 = 0
maior18 = 0

while resposta in "Ss":
    sexo = str(input("SEXO [M/F]: ")).strip().upper()
    idade = int(input("IDADE: "))
    resposta = str(input("Voce quer cadastra mais pessoas? "))
    if idade > 18:
        maior18 += 1

    elif sexo == "M":
        homens_cadastrado += 1

    elif sexo == "F" and idade < 20:
        mulher_menos20 += 1
        
print("PESSOAS CADSTRADAS COM MAIOR DE 18 ANOS {}".format(maior18))
print("homens cadastrados {}".format(homens_cadastrado))
print("mulher com menos de 20 anos cadastradas {}".format(mulher_menos20))