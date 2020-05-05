# This Python file uses the following encoding: utf-8
import os, sys, math

num1 = int (input("Digite um número de 1 a 7: "))

if num1 > 7:
    dia = "número inválido"
elif num1 == 1 :
    dia = "Domingo"    
elif num1 == 2 :
    dia = "Segunda"     
elif num1 == 3 :
    dia = "Terça"     
elif num1 == 4 :
    dia = "Quarta" 
elif num1 == 5 :
    dia = "Quinta" 
elif num1 == 6 :
    dia = "Sexta" 
elif num1 == 7 :
    dia = "Sábado"    


print("O dia é : " + str(dia))                 