# crie a tabuada usando o while

resposta = 0

while True:
    resposta = int(input("Digite um numero para saber a tabuada => "))
    if resposta < 0:
        break
    for c in range(1,11):
        print("{} x {} = {}".format(resposta, c, resposta*c))
print("numero invalido. o programa noa ler numeros negativos.")