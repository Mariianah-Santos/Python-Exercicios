# crie um codigo em lista e pergunte 4 vezes para o usuario digitar um numero. 
# mostre todos os numeros digitados, quantas vezes o numero 9 foi digitado. 
# Mostre se o numero 3 foi digitado e quais as posições.
numero = (int(input("Numero 1º: ")),
        int(input("Numero 2º ")), 
        int(input("Numero 3º: ")), 
        int(input("Numero 4º: ")))
print("Os numeros digitados foram {}".format(numero))
print("O numero 9 foi digitados {}".format(numero.count(9)))
if 3 in numero:
    print("O numero 3 contém na lista")
   
else:
    print("o umero 3 não esta na lista")