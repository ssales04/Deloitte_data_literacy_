# -*- coding: utf-8 -*-
"""Análise de dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JiL79Z-xudGbFH9vgE12BzHAvskcir1H
"""

import pandas as pd

from google.colab import files
uploaded = files.upload()

clientesBanco = pd.read_csv('ClientesBanco.csv', encoding = 'latin-1')

display(clientesBanco)

clientesBancoSemNumCliente = clientesBanco.drop('CLIENTNUM', axis = 1)

display (clientesBancoSemNumCliente)

somaLimiteDisponivel = clientesBancoSemNumCliente['Limite Disponível'].sum()
print(somaLimiteDisponivel)

somaLimiteDisponivelEducacao = clientesBancoSemNumCliente[['Educação','Limite Disponível']].groupby('Educação').sum()
display (somaLimiteDisponivelEducacao)

contadorTodasColunas = pd.DataFrame(clientesBanco)

print(contadorTodasColunas.count())

countEducacao = clientesBanco['Educação'].value_counts()
print(countEducacao)