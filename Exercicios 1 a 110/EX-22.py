# crie um codigo que pergnte o nome completo e mostre em MAIUSCULO, MENUSCULOS, total de letras e quantas letras tem o primeiro nome

nome =str(input('QUALO SEU NOME? ')).strip()
print('O NOME COMPLETO DO ÚSUARIO É', nome)
print('MAIUSCÚLO:', nome.upper())
print('MINUSCÚLO:', nome.lower())
print('TOTAL DE LETRAS:', len(nome))
