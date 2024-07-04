# crei um codigo que peça para o usuario digitar um numero e pergunte se ele(a) quer digitar mais
# mostre a ordem decrescente
# mostra quantos numeros foram dgitados
# mostra se o numero 5 foi digitado ou nao

lista = []
resposta = "S"
numeros = 0
cont = 0
while resposta in "S":
    numeros = int(input("Informe um numero => "))
    lista.append(numeros)
    resposta = str(input("Digitas mais? [S/N] => ")).upper().split()[0]
    cont += 1
if 5 in lista:
    print("o numero 5 foi digitado")
else:
    print("o nuemro 5 nao foi digitado")

print("foram digitados {} numeros".format(cont))
lista.sort(reverse=True)
print("a ordem decrescente é {}".format(lista))