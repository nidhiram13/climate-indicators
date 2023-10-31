import os
import sys
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


cwd = os.getcwd()

df = pd.read_csv('Tropopause_9500_16000.csv')
df.replace(0, np.nan, inplace=True)

#5 year intervals

df_1990 = df[df['Year'] < 1995]
df_1990 = df_1990.groupby('Daynum').median()
df_1990.to_csv('Tropo5yr_1990.csv')

df_1995 = df[(df['Year'] >= 1995) & (df['Year'] < 2000)]
df_1995 = df_1995.groupby('Daynum').median()
df_1995.to_csv('Tropo5yr_1995.csv')

df_2000 = df[(df['Year'] >= 2000) & (df['Year'] < 2005)]
df_2000 = df_2000.groupby('Daynum').median()
df_2000.to_csv('Tropo5yr_2000.csv')

df_2005 = df[(df['Year'] >= 2005) & (df['Year'] < 2010)]
df_2005 = df_2005.groupby('Daynum').median()
df_2005.to_csv('Tropo5yr_2005.csv')

df_2010 = df[(df['Year'] >= 2010) & (df['Year'] < 2015)]
df_2010 = df_2010.groupby('Daynum').median()
df_2010.to_csv('Tropo5yr_2010.csv')

df_2015 = df[(df['Year'] >= 2015) & (df['Year'] < 2020)]
df_2015 = df_2015.groupby('Daynum').median()
df_2015.to_csv('Tropo5yr_2015.csv')

df_2020 = df[(df['Year'] >= 2020) & (df['Year'] < 2025)]
df_2020 = df_2020.groupby('Daynum').median()
df_2020.to_csv('Tropo5yr_2020.csv')

fullavg = df.groupby('Daynum').median()
fullavg.to_csv('Tropo5yr_all.csv')




#print (df_2000)


#boxplot = df.boxplot(column=df,by=df['Year'])



