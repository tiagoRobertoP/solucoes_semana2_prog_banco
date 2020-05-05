# This Python file uses the following encoding: utf-8
import os, sys, math

nota1 = float (input("Digite a nota 01 : "))
nota2 = float (input("Digite a nota 02 : "))
media = (nota1 + nota2) / 2

if media < 7 :
    print("Repovado")   
elif media == 10 :
    print("Aprovado com distinção")
else :
    print("Aprovado")