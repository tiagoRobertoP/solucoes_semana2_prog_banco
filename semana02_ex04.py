# This Python file uses the following encoding: utf-8
import os, sys, math


num1 = float (input("Digite o primeiro número: "))
num2 = float (input("Digite o segundo número: "))
operacao = int (input("digite 1 para soma,2 para subtração, 3 para multiplicação ou 4 para divisão"))

if operacao == 1 :
    resultado = num1 + num2
elif operacao == 2 :
    resultado = num1 - num2  
elif operacao == 3 :
    resultado = num1 * num2 
elif operacao == 4 :
    resultado = num1 / num2     

if resultado % 2 == 0 :
    parImpar = "par"
else :
        parImpar = "impar"

if resultado < 0 :
    positivoNegativo = "negativo"
else:
        positivoNegativo = "positivo"

ponto = False
for i in str(resultado) :
    if i =="." :
        ponto = True
if ponto == True :
    decimalInteiro = "decimal"                       
else:
        decimalInteiro = "inteiro"

print("resultado = " + str(resultado))
print(str(parImpar))
print(str(positivoNegativo))
print(str(decimalInteiro))