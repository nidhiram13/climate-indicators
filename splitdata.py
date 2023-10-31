import seaborn as sns
import pandas as pd
import numpy as np

df  = pd.read_csv('DayAvg_5yr_1990.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('1990_1.csv')
df_2.to_csv('1990_2.csv')
df_3.to_csv('1990_3.csv')
df_4.to_csv('1990_4.csv')

df  = pd.read_csv('DayAvg_5yr_1995.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('1995_1.csv')
df_2.to_csv('1995_2.csv')
df_3.to_csv('1995_3.csv')
df_4.to_csv('1995_4.csv')

df  = pd.read_csv('DayAvg_5yr_2000.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('2000_1.csv')
df_2.to_csv('2000_2.csv')
df_3.to_csv('2000_3.csv')
df_4.to_csv('2000_4.csv')

df  = pd.read_csv('DayAvg_5yr_2005.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('2005_1.csv')
df_2.to_csv('2005_2.csv')
df_3.to_csv('2005_3.csv')
df_4.to_csv('2005_4.csv')

df  = pd.read_csv('DayAvg_5yr_2010.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('2010_1.csv')
df_2.to_csv('2010_2.csv')
df_3.to_csv('2010_3.csv')
df_4.to_csv('2010_4.csv')

df  = pd.read_csv('DayAvg_5yr_2015.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('2015_1.csv')
df_2.to_csv('2015_2.csv')
df_3.to_csv('2015_3.csv')
df_4.to_csv('2015_4.csv')


df  = pd.read_csv('DayAvg_5yr_2020.csv')
df_1 = df.iloc[:91,:]
df_2 = df.iloc[91:182,:]    
df_3 = df.iloc[182:273,:]
df_4 = df.iloc[273:,:]
df_1.to_csv('2020_1.csv')
df_2.to_csv('2020_2.csv')
df_3.to_csv('2020_3.csv')
df_4.to_csv('2020_4.csv')