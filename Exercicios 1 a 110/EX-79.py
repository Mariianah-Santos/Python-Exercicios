# crie um codigo que pergunte o numero e se o usuario quer digitar mais.
# mostre a ordem dos numeros
# mostra se o numero ja foi digitado 

numeros = 0 
lista = list()
resposta = "S"

while resposta in "S":
    numeros = int(input("Informe qualquer numero => "))
    if numeros not in lista:
        lista.append(numeros)
        print("Numero adicionado com sucesso")
    else:
        print("O numero já contem na lista")
    resposta = str(input("Quer digitar mais algum numero? [S/N] => ")).upper().split()[0]
print("a ordem de todos os numeros digitado é {}".format(sorted(lista)))