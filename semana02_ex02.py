# This Python file uses the following encoding: utf-8
import os, sys, math

nota1 = float (input("Digite a nota 01 : "))
nota2 = float (input("Digite a nota 02 : "))
media = (nota1 + nota2) / 2

if media <= 4 :
    conceito = 'E'
elif media <= 6 :
    conceito = 'D'
elif media <= 7.5 :
    conceito = 'C'
elif media <= 9 :
    conceito = 'B'
elif media <= 10 :
    conceito = 'A'

if media >= 7.5 :
    resultado = "APROVADO"
else :
    resultado = "REPROVADO"        

print("====   RESULTADO   ====")
print("nota 1 = " + str(nota1) + "  Nota 2 = " + str(nota2))
print("A média é " + str(media))
print("O conceito é " + str(conceito))
print("O resultado é " + str(resultado))
