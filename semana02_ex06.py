# This Python file uses the following encoding: utf-8
import os, sys, math

tipo = int (input("Escolha  otipo de carne: 1 para file Duplo,2 para Alcatra ou 3 para Picanha : "))
quantidade = float (input("digite a quantidade em quilos de carne desejada : "))
pagamento = int (input("Forma pagamento : 1-Cartão Tabajara ou 2-Outro : "))


if tipo == 1:
    if quantidade > 5:
        total = quantidade * 5.80
    else:
        total = quantidade * 4.90
    print('File Duplo com Qtd:' + str(quantidade) + "e total de : R$" + str(total))
    
if tipo == 2:
    if quantidade > 5:
        total = quantidade * 6.80
    else:
        total = quantidade * 5.90
    print('Alcatra com Qtd:' + str(quantidade) + "e total de : R$" + str(total))

if tipo == 3:
    if quantidade > 5:
        total = quantidade * 7.80
    else:
        total = quantidade * 6.90
    print('Picanha com Qtd:' + str(quantidade) + "e total de : R$" + str(total))



if pagamento == 1 :
    print("pagamento com cartão Tabajara")
    desconto = total * .05
    print("desconto de : " + str(desconto))
    print("valor a pagar de : " + str(total-desconto))
else:
        print("pagamento com Outra Forma")
        print("valor a pagar de : " + str(total))