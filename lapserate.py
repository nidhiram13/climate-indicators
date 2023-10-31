import os
import sys
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


cwd = os.getcwd()

##make dataframe with index for each day number per year
startyear = 1990
endyear = 2023
Time = '00'

yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear)+1, dtype=int)])
daylist = np.array([np.linspace(1, 24000, 24000, dtype=int)])

dayArr = np.empty(365*((endyear-startyear)+1), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)

for i in range(0,dayArr.size,yearlist.size):
    dayArr[i:(i+(endyear-startyear)+1)] = dayiter
    dayiter +=1
Harr = np.zeros_like(dayArr, dtype = int)
Tarr = np.zeros_like(dayArr, dtype = int)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), Harr, Tarr]).T
df.columns=['Daynum','Year','Height','Temperature']
df.replace(0, np.nan, inplace=True)

##Find file and open into a dataframe
for i, row in df.iterrows():

    datestr = (datetime.strptime(str(df['Year'][i]) + "-" + str(df['Daynum'][i]), "%Y-%j").strftime("%b-%d-%Y")).split('-')
    filename = 'Profile_PIT_'+datestr[2]+'_'+datestr[0]+'_'+datestr[1]+'_'+Time+'Z'+'.txt'
    if os.path.isfile('/Users/nidhiram/PGSS/Profiles'+filename): #if the file exists then open file to extract data

        colnames =['Press','Height','Temp','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
        try:
            profile = pd.read_fwf('/Users/nidhiram/PGSS/Profiles'+filename,  skiprows=5, header = 0, names = colnames)
        except:
            df['Temperature'].iat[i] = np.nan
            df['Height'].iat[i] = np.nan
        
        else:
            df['Temperature'].iat[i] = profile.loc['Temp']
            df['Height'].iat[i] = profile.loc['Height']
            df['dT'] = df['Temperature'].diff()
            df['dZ'] = df['Height'].diff(axis=1)
            df['dZ'] = df['dZ']/1000
            df['dt/dZ'] = df['dT']/df['dZ']
df.to_csv('testBoundData_Height1_.csv')     




def main():

    print('test')

if __name__ == "__main__": 
  # calling main function 
  main() 