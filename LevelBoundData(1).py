
import os
import sys
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


cwd = os.getcwd()

##make dataframe with index for each day number per year
startyear = 2020
endyear = 2020
Time = '00'

MinHeight = 10 #Minumum bound of geopotential height in meters
MaxHeight = 500 #Maximum bound of geopotential height in meters

yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear)+1, dtype=int)])
daylist = np.array([np.linspace(1, 365, 365, dtype=int)])

dayArr = np.empty(365*((endyear-startyear)+1), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)

for i in range(0,dayArr.size,yearlist.size):
    dayArr[i:(i+(endyear-startyear)+1)] = dayiter
    dayiter +=1

Parr = np.zeros_like(dayArr, dtype = int)
Tarr = np.zeros_like(dayArr, dtype = int)
RHarr = np.zeros_like(dayArr,dtype = int)
WSarr = np.zeros_like(dayArr,dtype = int)

#print(yearArr.size)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), Parr, Tarr, RHarr, WSarr]).T
df.columns=['Daynum','Year','Pressure','Temperature','Relative Humidity','Wind Speed']
df.replace(0, np.nan, inplace=True)

##Find file and open into a dataframe
for i, row in df.iterrows():

    datestr = (datetime.strptime(str(df['Year'][i]) + "-" + str(df['Daynum'][i]), "%Y-%j").strftime("%b-%d-%Y")).split('-')
    filename = 'Profile_PIT_'+datestr[2]+'_'+datestr[0]+'_'+datestr[1]+'_'+Time+'Z'+'.txt'
    #print(filename)

    if os.path.isfile(cwd+'/Profiles/'+filename): #if the file exists then open file to extract data
        #print(cwd+'/Profiles/'+filename)

        colnames =['Press','Height','Temp','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
        try:
            profile = pd.read_fwf(cwd+'/Profiles/'+filename,  skiprows=5, header = 0, names = colnames)
            height = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'Height'].mean()
        except:

            df['Pressure'].iat[i] = np.nan
            df['Temperature'].iat[i] = np.nan
            df['Relative Humidity'].iat[i] = np.nan
            df['Wind Speed'].iat[i] = np.nan
        
        else:
            df['Pressure'].iat[i] = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'Press'].mean()
            df['Temperature'].iat[i] = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'Temp'].mean()
            df['Relative Humidity'].iat[i] = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'RH'].mean()
            df['Wind Speed'].iat[i] = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'WS'].mean()

  

df.to_csv('20BoundData_Height_'+str(MinHeight)+'_'+str(MaxHeight)+'.csv')     
            

def main():

    print('test')

if __name__ == "__main__": 
  # calling main function 
  main() 