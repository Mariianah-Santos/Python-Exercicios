exp = str(input('DIGITE SUA EXPRESSO => '))
pilha = []
for simb in exp:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('EXPRESSÃO VÁLIDA!!')
else:
    print('EXPRESSÃO INVÁLIDA!!')