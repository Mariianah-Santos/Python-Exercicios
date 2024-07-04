# crie um codigo usando o WHILE e o codigo deve mostra a soma dos numeros digitados e so vai parar quando o usuario digitar '999' e qunado for soma nao pode conta com o '999'

soma = 0 
cont = 0 
numero = 0 
print("PARA PARAR BASTAR DIGITA '999'")
while numero != 999:
    numero = int(input("Digite um valor => "))
    if numero != 999:
        soma += numero
        cont += 1

print("A soma dos numeros é {} e foram digitados {}".format(soma, cont))