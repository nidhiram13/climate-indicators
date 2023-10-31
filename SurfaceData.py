
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
SurfaceHeight = 500 #Geopotential height

yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear), dtype=int)])
daylist = np.array([np.linspace(1, 365, 365, dtype=int)])

#dayArr = np.tile(daylist, (endyear-startyear))
dayArr = np.empty(365*(endyear-startyear), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)

#print(yearArr.shape)

for i in range(0,dayArr.size,yearlist.size):
    dayArr[i:(i+endyear-startyear)] = dayiter
    dayiter +=1

Parr = np.zeros_like(dayArr, dtype = int)
Tarr = np.zeros_like(dayArr, dtype = int)
RHarr = np.zeros_like(dayArr,dtype = int)
WSarr = np.zeros_like(dayArr,dtype = int)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), Parr, Tarr, RHarr, WSarr]).T
df.columns=['Daynum','Year','Pressure','Temperature','Relative Humidity','Wind Speed']
#print (df['Daynum'])

#df.replace(0, np.nan, inplace=True)

#Find file and open into a dataframe
for i in range(365*(endyear-startyear)):

    datestr = (datetime.strptime(str(df['Year'][i]) + "-" + str(df['Daynum'][i]), "%Y-%j").strftime("%b-%d-%Y")).split('-')
    filename = 'Profile_PIT_'+datestr[2]+'_'+datestr[0]+'_'+datestr[1]+'_'+Time+'Z'+'.txt'

    if os.path.isfile(cwd+'/Profiles/'+filename): #if the file exists then open file to extract data
        #print(cwd+'/Profiles/'+filename)

        colnames =['Press','Height','Temp','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
        try:
            profile = pd.read_fwf(cwd+'/Profiles/'+filename,  skiprows=5, header = 0, names = colnames)
            height = profile.loc[profile['Height'] <= SurfaceHeight,'Height'].mean()
            
        except:
            df['Pressure'][i] = np.nan
            df['Temperature'][i] = np.nan
            df['Relative Humidity'][i] = np.nan
            df['Wind Speed'][i] = np.nan
            
        
        else:
            df['Pressure'][i] = profile.loc[profile['Height'] <= SurfaceHeight,'Press'].mean()
            df['Temperature'][i] = profile.loc[profile['Height'] <= SurfaceHeight,'Temp'].mean()
            df['Relative Humidity'][i] = profile.loc[profile['Height'] <= SurfaceHeight,'RH'].mean()
            df['Wind Speed'][i] = profile.loc[profile['Height'] <= SurfaceHeight,'WS'].mean()
       
    

df.to_csv('SurfaceData.csv')     
            





#print(dayArr)
#np.savetxt('test.out', dayArr, delimiter=',')   # X is an array





def main():

    print('test')

if __name__ == "__main__": 
  # calling main function 
  main() 