# -*- coding: utf-8 -*-
"""Exercício11.PY

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16SGuEfCIZLLwLO9lWn557sdiYiVj4kSC
"""

# EXERCÍCIO 1 - ESCREVA UMA LAMBDA QUE RETORNE O DOBRO DE UM NÚMERO.

numero = [10]
dobro = list(map(lambda x:x**2,numero))

print('numero = {}''\n' 'dobro = {}'.format(numero,dobro))

# EXERCÍCIO 2 - ESCREVA UMA LAMBDA QUE CALCULE A SOMA DE DOIS NÚMEROS.

soma = lambda x,y : x + y
resultado = soma (5,10)
print('A soma é igual a = {}'.format(resultado))

# EXERCÍCIO 3 - ESCREVA UMA LAMBDA QUE VERIFIQUE SE OS NÚMEROS SÃO PARES.

verificar = lambda x: x % 2 == 0
resultado = verificar (10)

print(resultado)

# EXERCÍCIO 4 - ESCREVA UMA LAMBDA QUE CONVERTA UMA STRING EM MAIUSCÚLAS.

converter = lambda palavra: palavra.upper()
resultado = converter('henrique buontempi bonafé')

print(resultado)

# EXERCÍCIO 5 - ESCREVA UMA LAMBDA QUE DE O RESULTADO DO PRODUTO DE TRÊS NÚMEEROS.

from functools import reduce

lista = [10,20,15]
produto = reduce (lambda x,y: x * y,lista)

print('Lista = {}''\n''Produto = {}'.format(lista,produto))