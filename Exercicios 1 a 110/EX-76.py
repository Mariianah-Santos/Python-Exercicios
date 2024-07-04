# crie um codigo usando listas e faça uma tabela de preço. Use o for para alinha e organizar a tabela


print('=/='*20)
print('{:^60}'.format('LISTAGEM DE PREÇO'))
print('=/='*20)
lista = ('Lápis',1.75,
         'Borracha',2.00,
         'Caderno',15.00,
         'Estojo',25.00,
         'Transferidor',4.00,
         'Compasso',9.99,
         'Mochila',120.32,
         'Caneta',22.30,
         'Livros',34.90)
for item in range(0, len(lista)):
        if item % 2 == 0:
                print(f'{lista[item]:.<30}', end='')
        else:
                print(f'R${lista[item]:<10}')
print('=/='*20)