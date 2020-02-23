#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:48:08 2020

@author: itamar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv("Metro_Interstate_Traffic_Volume.csv")

df['day'] = (pd.to_datetime(df['date_time']).dt.day).astype(int)
df['month'] = (pd.to_datetime(df['date_time']).dt.month).astype(int)
df['hour'] = (pd.to_datetime(df['date_time']).dt.hour).astype(int)

df.drop(columns = ['date_time'],inplace = True)

df.isnull().sum()
df.duplicated().sum()
df = df.drop_duplicates()

stats = df.describe(include = "all")

encoder = LabelEncoder()
df['holiday'].loc[df['holiday'] == 'None'] = str(0)
loc = df['temp'].loc[df['temp'] == 0].index
print(loc)
value = loc[0]
lol = df['temp'].iloc[loc[0]-2:loc[3]+2]
df['temp'].loc[df['temp'] == 0] = np.nan
df ['temp'] = df['temp'].fillna(method = 'ffill')

df['rain_1h'].loc[df['rain_1h'] == 9831.0] = np.nan
print(df.isnull().sum())
df ['rain_1h'] = df['rain_1h'].fillna(method = 'ffill')
print(df.isnull().sum())



#df['holiday'].loc[df['holiday'] != 0] = 1
"""
na minha cabeça, se eu boto o dia a hora e o mes, dizer o feriado nao faz sentido
só botar 0 ou 1 já é suficientye
"""
df['holiday'] = encoder.fit_transform(df['holiday'])
df['weather_main'] = encoder.fit_transform(df['weather_main'])
df['weather_description'] = encoder.fit_transform(df['weather_description'])


transformer = ColumnTransformer(transformers=[("OneHot",OneHotEncoder(),[5,6])],remainder='passthrough')
df = transformer.fit_transform(np.asarray(df).tolist())
df = df.astype('float64')
df = pd.DataFrame(df)