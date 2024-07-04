# crie um codigo usando lista. Pegue 20 times que estão no top e mostre os 5 primeiros colocados. Os 4 ultimos na posição. 

time = ('Palmeiras', 'Internacional', 'Flamengo', 'Fluminense', 'Corinthians', 'Athletico-PR',
'Atlético-MG', 'América-MG', 'Goiá', 'Santos', ' Bragantino',
'Botafogo', 'São Paulo', ' Ceará', 'Fortaleza', ' Coritiba', 'Cuiabá',
 'Avaí', 'Atlético-GO', 'Juventude')
print ("Lista dos 5 primeros")
for posicao in range (0, 5):
    print(f"{posicao+1}º", time[posicao])

for posicao_ultimos in range(16, 20):
    print(f"{posicao_ultimos+1}º", time[posicao_ultimos])

print('ESTA NA POSIÇÃO ', end= ' ')
print(time.index("Flamengo"))
print('='*40)
print(sorted(time))    
