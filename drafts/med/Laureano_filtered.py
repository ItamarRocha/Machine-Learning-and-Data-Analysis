#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 16:27:59 2020

@author: itamar
"""

import pandas as pd


# importa o arquivo
df = pd.read_csv('Epidemiológico H. Laureano - Pacientes - Página1.csv',header = 1)

#retira os atributos que tem dados faltantes no diagnostico e na data de nascimento
df.dropna(axis = 0, subset = ['diagnostico','data','anamapato'],inplace = True)

#pega os indices que sao NE ou D/N? na data de nascimento
ne_index = df.loc[(df['data'] == 'NE') | (df['data'] == 'D/N?')].index

# dropa esses indices
df = df.drop(index = ne_index)

# pegas os indices que nao foram encontrados ou NE no diagnostico
indexes = df.loc[(df['diagnostico'] == 'NE') | (df['diagnostico'] == "Não encontrado no sistema")].index

#dropa esses indices.
df = df.drop(index = indexes)

#faz um arquivo csv com essas alterações
#df.to_csv("v1.csv")

lista = []# lista que vai pegar todos os atributos que nao tem nenhuma das palavras especificadas a seguir neles
for anatomo,anamto_index in zip(df['anamapato'],df['anamapato'].index):
    print(anatomo,anamto_index)
    if not ("neo" in anatomo or "granulomatosa" in anatomo or "oma" in anatomo or "omas" in anatomo or "neoplasia" in anatomo or "tumor" in anatomo):
        lista.append(anamto_index)

df = df.drop(index = lista) #dropa os que nao tem as palavras ditas

#pega os indices dos duplicados tanto em código quanto em nome
dupli_index = df.loc[df.duplicated(subset = ['codigo','nome']) == True].index

# so pra visualizar
duplicated = df.loc[dupli_index]

# dropa os duplicados
df = df.drop(index = dupli_index)


df.to_csv("filtered_data.csv")