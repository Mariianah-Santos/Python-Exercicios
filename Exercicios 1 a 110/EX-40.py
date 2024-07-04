# crie um codigo deaprovação de notas. maior ou igual a 7 "aprovado". Menor ou igual a 6 "RECUPERAÇÃO" abaixo disso "REPROVADO"

nota1 = float(input("Qual sua primeira nota => "))
nota2 = float(input("Qual sua segunda nota => "))
media = (nota1+nota2)/2

if media >= 7:
    print("APROVADO")
if media >= 5 and media <= 6:
    print("RECUPERAÇÃO")
if media < 5:
    print("REPROVADO")

print("SUA MEDIA FOI {}".format(media))
