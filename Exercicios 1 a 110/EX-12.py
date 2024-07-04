# CRIE UM CODIGO QUE IRÁ PERGNTA O VALOR DO PRODUTO E TERÁ UM DESCONTO DE 5%

produtoOriginal = float(input("Digite o valor do produtor R$"))
valor_novo = produtoOriginal - (produtoOriginal * 5 / 100)
print(f"O produtor sem desconto é R${produtoOriginal}, O valor com desconto está custando R${valor_novo}")