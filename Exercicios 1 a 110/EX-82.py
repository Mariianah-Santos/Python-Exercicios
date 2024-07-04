# crie um codigousando listas para mostas numeros pares, impares e todos os valores digitados

resposta = "S"
par = list()
impare = list()
numeros = list()
cont = 0
while resposta in "S":
    numeros.append(int(input("digite um valor => ")))
    cont += 1
    resposta = str(input("continiar? [SN] => ")).upper().split()[0]
for i, saber in enumerate(numeros):
    if saber % 2 == 0:
        par.append(saber)
    elif saber % 2 == 1:
        impare.append(saber)
print(f'OS NUMEROS IMPARES SÃO {impare}')
print(f'OS NUMEROS PARES SÃO {par}')
print('TODOS OS VALORES SÃO {} E FORAM DIGITADO {}'.format(numeros, cont))