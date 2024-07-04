# crie um codigo de pagamento de produto, se será em cartao(dividido), debito, dinheiro. A partir de 3x o valor ganhará 20% de juros 

produto = float(input("O valor do produto R$"))
print("""Informe qual o tipo de pagamento
[1] CRÉDITO 2X SEM JUROS
[2] DINHEIRO/CHEQUE (10% DE DESCONTO)
[3] DÉBITO
[4] CRÉDITO 3X OU + COM 20% DE JUROS""")
tipo_pagamento = int(input("=> "))
if tipo_pagamento == 1:
    produto_parcelado = produto / 2
    print("A parcelas ficam de R${} O valor original é {}".format(produto_parcelado, produto))
elif tipo_pagamento == 2:
    produto10 = produto - (produto * 10 / 100)
    print(f"Produto pago com dinheiro. Valor a pagar R${produto10} valor orginal R${produto}")
elif tipo_pagamento == 3:
    print("A pagar R${}".format(produto))
elif tipo_pagamento == 4:
    produto30 = produto + (produto * 20 / 100)
    print(f"A pagar R${produto30} valor orignial R${produto}")
    
