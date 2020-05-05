# This Python file uses the following encoding: utf-8
import os, sys, math

ano = int (input("Digite o ano para ver se é bissexto: "))

if ano % 400 == 0 or (ano % 4 == 0) and (ano % 100 != 0)  :
    bissexto = " é bissexto"
else :
    bissexto = " não é bissexto"

print("O ano " + str(ano) + str(bissexto))        