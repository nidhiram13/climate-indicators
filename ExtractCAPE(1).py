import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def extract_cape(file_path):
    cape_value = None
    with open(file_path, 'r') as file:
        
        for line in file:
            print(cape_value)
            
            if line.startswith('      Convective Available Potential Energy:'):
                cape_value = float(line.split(':')[1].strip())
                
                break
    return cape_value

#Get working directory
cwd = os.getcwd()

##make dataframe with index for each day number per year
startyear = 1990
endyear = 2023
Time = '00'

yearlist = np.array([np.linspace(startyear, endyear, (endyear-startyear)+1, dtype=int)])
daylist = np.array([np.linspace(1, 365, 365, dtype=int)])

dayArr = np.empty(365*((endyear-startyear)+1), dtype = int)
dayiter = 1
yearArr = np.tile(yearlist,365)


for i in range(0,dayArr.size,yearlist.size):
    dayArr[i:(i+(endyear-startyear)+1)] = dayiter
    dayiter +=1

valArr = np.zeros_like(dayArr, dtype = int)

df = pd.DataFrame(data = [dayArr, np.squeeze(yearArr), valArr]).T
df.columns=['Daynum','Year','CAPE']
df.replace(0, np.nan, inplace=True)

##Find file and open into a dataframe
for i, row in df.iterrows():

    datestr = (datetime.strptime(str(df['Year'][i]) + "-" + str(df['Daynum'][i]), "%Y-%j").strftime("%b-%d-%Y")).split('-')
    filename = 'MetIndices_PIT_'+datestr[2]+'_'+datestr[0]+'_'+datestr[1]+'_'+Time+'Z'+'.txt' ##example: MetIndices_PIT_1990_Aug_19_00Z.txt
    #print(filename)

    path = cwd+'/Indices/'+filename

    if os.path.isfile(path): #if the file exists then open file to extract data

        #print(path)
   
        try:
            val = extract_cape(path)
            print(val)

        except:

            df['CAPE'].iat[i] = np.nan
        
        else:
            df['CAPE'].iat[i] = val

df.to_csv('Indices_Extract_'+'CAPE11.csv')