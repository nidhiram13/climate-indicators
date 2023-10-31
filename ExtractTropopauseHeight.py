
import os
import sys
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

np.set_printoptions(threshold=np.inf)
cwd = os.getcwd()

##make dataframe with index for each day number per year
startyear = 1990
endyear = 2023
Time = '12'

MinHeight = 9500 #Minumum bound of geopotential height in meters
MaxHeight = 16000 #Maximum bound of geopotential height in meters



yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear)+1, dtype=int)])
daylist = np.array([np.linspace(1, 365, 365, dtype=int)])

#print(yearlist)

dayArr = np.empty(365*((endyear-startyear)+1), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)


for i in range(0,dayArr.size,yearlist.size):

    dayArr[i:(i+(endyear-startyear)+1)] = dayiter
    dayiter +=1


HeightArr = np.zeros_like(dayArr, dtype = int)
PressArr = np.zeros_like(dayArr, dtype = int)
TempArr = np.zeros_like(dayArr,dtype = int)
WindArr = np.zeros_like(dayArr,dtype = int)
LapseArr = np.zeros_like(dayArr,dtype = int)

# #print(yearArr.size)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), HeightArr, PressArr, TempArr, WindArr, LapseArr]).T
df.columns=['Daynum','Year','TropoHeight','TropoPress','TropoTemp','TropoWind', 'LapseRate']
df.replace(0, np.nan, inplace=True)

#print (df)

##Find file and open into a dataframe
for index, row in df.iterrows():

    datestr = (datetime.strptime(str(df['Year'][index]) + "-" + str(df['Daynum'][index]), "%Y-%j").strftime("%b-%d-%Y")).split('-')
    filename = 'Profile_PIT_'+datestr[2]+'_'+datestr[0]+'_'+datestr[1]+'_'+Time+'Z'+'.txt'
    #print(filename)

    if os.path.isfile(cwd+'/Profiles/'+filename): #if the file exists then open file to extract data
        #print(cwd+'/Profiles/'+filename)

        colnames =['Press','Height','Temp','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
        try:
            profile = pd.read_fwf(cwd+'/Profiles/'+filename,  skiprows=5, header = 0, names = colnames)
            #height = profile.loc[(profile['Height'] <= MaxHeight) & (profile['Height'] > MinHeight),'Height'].mean()
        except:

            df['TropoHeight'].iat[index] = np.nan
            df['TropoPress'].iat[index] = np.nan
            df['TropoTemp'].iat[index] = np.nan
            df['TropoWind'].iat[index] = np.nan
            df['LapseRate'].iat[index] = np.nan
        else:

            profile['dT'] = ''
            profile['dz']  = ''
            profile['dTdz'] = ''

            for i, row in profile.iterrows():

                profile['dT'].iat[i] = (profile['Temp'].iat[i]+273.15)-(profile['Temp'].iat[i-1]+273.15)
                profile['dz'].iat[i] = profile['Height'].iat[i]-profile['Height'].iat[i-1]
            
            profile['dTdz'] = (profile['dT']/profile['dz'])*1000

           

            profile['dTdz_smth'] = profile['dTdz'].rolling(window=2, center=True, win_type='boxcar').mean()

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

                    if profile['dTdz_smth'].iat[i-1] >= float(-2) and profile['dTdz_smth'].iat[i] >= float(-2) and profile['dTdz_smth'].iat[i+1] >= float(-2) :

                        matchrow = i
                        #print(str(datestr)+' '+str(profile['Height'].iat[i])+' '+str(matchrow))
                        break

            if(matchrow!=0): 

                #print(profile['Height'].iat[matchrow])
                df['TropoHeight'].iat[index] = profile['Height'].iat[matchrow]
                df['TropoPress'].iat[index] = profile['Press'].iat[matchrow]
                df['TropoTemp'].iat[index] = profile['Temp'].iat[matchrow]
                df['TropoWind'].iat[index] = profile['WS'].iat[matchrow]
                df['LapseRate'].iat[index] = -1*profile['dTdz_smth'].iat[matchrow]

            


#print(df)

df.to_csv('Tropopause_'+str(MinHeight)+'_'+str(MaxHeight)+'.csv')     
            

# def main():

#     print('test')

# if __name__ == "__main__": 
#   # calling main function 
#   main() 