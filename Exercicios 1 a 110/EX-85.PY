lista = list()
par = list()
impar = list()
for c in range (1, 8):
    lista.append(int(input(f'DIGITE O {c}º VALOR => ')))
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'PARES => {sorted(par)} ')
print(f'IMPARES => {sorted(impar)} ')
print(f'LISTA COMPLETA DIGITADA => {sorted(lista)}')

# ou

lista = [[], []]
num = 0
for c in range (1, 8):
    num = (int(input(f'DIGITE O {c}º VALOR => ')))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 == 1:
        lista[1].append(num)
print(f'PARES => {sorted(lista[0])} ')
print(f'IMPARES => {sorted(lista[1])} ')
print(f'LISTA COMPLETA DIGITADA => {sorted(lista)}')