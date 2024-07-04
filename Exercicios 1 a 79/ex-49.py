# 4. Escreva um programa que solicite ao usuário o valor de uma compra e
# calcule o valor final da compra com um desconto de 10%.

produto = float(input("informe o valor do produto R$"))
produto_10 = produto - (produto * 10 /100)
print("R${}".format(produto_10))