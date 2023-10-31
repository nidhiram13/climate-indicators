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
Time = '12'

MinHeight = 5000 #Minumum bound of geopotential height in meters
MaxHeight = 10000 #Maximum bound of geopotential height in meters

yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear)+1, dtype=int)])
daylist = np.array([np.linspace(1, 365, 365, dtype=int)])

dayArr = np.empty(365*((endyear-startyear)+1), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)

for i in range(0,dayArr.size,yearlist.size):
    dayArr[i:(i+(endyear-startyear)+1)] = dayiter
    dayiter +=1

Heightarr = np.zeros_like(dayArr, dtype = int)
Pressurearr = np.zeros_like(dayArr, dtype = int)
Temparr = np.zeros_like(dayArr,dtype = int)
WSarr = np.zeros_like(dayArr,dtype = int)
LRarr = np.zeros_like(dayArr,dtype=int)

#print(yearArr.size)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), Heightarr, Pressurearr, Temparr, WSarr, LRarr]).T
df.columns=['Daynum','Year', 'Height', 'Pressure','Temp','Wind Speed', 'LR']
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
            df['Height'].iat[i] = np.nan
            df['Pressure'].iat[i] = np.nan
            df['Temp'].iat[i] = np.nan
            df['Wind Speed'].iat[i] = np.nan
            df['LR'].iat[i] = np.nan
        else:
            profile['dT'] = ""
            profile['dZ']  = ""
            profile['dT/dZ'] = ""
  
            for i, row in profile.iterrows():

                profile['dT'].iat[i] = (profile['Temp'].iat[i]+273.15)-(profile['Temp'].iat[i-1]+273.15)
                profile['dZ'].iat[i] = profile['Height'].iat[i]-profile['Height'].iat[i-1]
            
            profile['dT/dZ'] = (profile['dT']/profile['dZ'])*1000

           

            profile['dT/dZ_smth'] = profile['dT/dZ'].rolling(window=2, center=True, win_type='boxcar').mean()

            # print(profile['dTdz_smth'])
                 
            # profile.plot(kind='line',
            # x= 'dTdz_smth',
            # y='Height',
            # color='red')
            # plt.show()
            # break

            matchrow = 0

            #print(profile.iterrows())

            #for i, row in profile.iterrows():
            for i in range(len(profile)-1):

                if profile['Height'].iat[i]>MinHeight and profile['Height'].iat[i]<MaxHeight:

                    if profile['dT/dZ_smth'].iat[i-1] >= float(-2) and profile['dT/dZ_smth'].iat[i] >= float(-2) and profile['dT/dZ_smth'].iat[i+1] >= float(-2) :

                        matchrow = i
                        #print(str(datestr)+' '+str(profile['Height'].iat[i])+' '+str(matchrow))
                        break

            if(matchrow!=0): 

                print(profile['Height'].iat[matchrow])
                df['Height'].iat[index] = profile['Height'].iat[matchrow]
                df['Pressure'].iat[index] = profile['Press'].iat[matchrow]
                df['Temp'].iat[index] = profile['Temp'].iat[matchrow]
                df['WS'].iat[index] = profile['WS'].iat[matchrow]
                df['LR'].iat[index] = -1*profile['dTdz_smth'].iat[matchrow]

            


#print(df)

df.to_csv('Tropopause_'+str(MinHeight)+'_'+str(MaxHeight)+'.csv')     
            

# def main():

#     print('test')

# if __name__ == "__main__": 
#   # calling main function 
#   main() 