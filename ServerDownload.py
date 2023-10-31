
#import requests
import sys
import urllib.request

from bs4 import BeautifulSoup
import requests
import datetime
import numpy as np
import pandas as pd



def RAMPDownload(argv):

    #input parameters
    sitename = argv[1]+'/'
    siteflag = 0

    print (argv)
    startdate = datetime.date.fromisoformat(argv[2])
    enddate = datetime.date.fromisoformat(argv[3])

    #empty pandas dataframe to hold data within datarange
    
    dtypes = np.dtype(
    [
        ("Datetime", str),
       #("Time_Local", str),
        #("UnixTime_Local", float),
        ("CO", float),
        ("SO2", float),
        ("NO2", float),
        ("Ozone", float),
        ("CO2", float),
        ("T", float),
        ("RH", float),
        ("PM", float),
    ]
    )

    df = pd.DataFrame(np.empty(0, dtype=dtypes))

    ##check if sitname exists
    startpage = urllib.request.urlopen('http://18.222.146.48/CMUAQ/data').read()
    soup = BeautifulSoup(startpage, 'html.parser')
    #headertag = soup.find_all('a') 

    for site in soup.find_all('a'):

        sitestr = site.get('href').strip()
 
        if sitestr == sitename :
            siteflag = 1
            #print('site match')

    if siteflag: ##if the site exists then find iterate through the list on the server and find the dates of interest
        
        startpage = urllib.request.urlopen('http://18.222.146.48/CMUAQ/data/'+sitename).read()
        soup = BeautifulSoup(startpage, 'html.parser')

        ##iterator for dataframe index
        dateiter = 0

        for date in soup.find_all('a'):
            
            datestr = date.get('href').strip()    
            datelist = datestr.split('-')

            if(len(datelist)>3):
                filedate = datetime.date(int(datelist[0]),int(datelist[1]),int(datelist[2]))
                if(filedate>=startdate and filedate<=enddate): #if the file date is within bounds then open and parse each line

                    response = requests.get('http://18.222.146.48/CMUAQ/data/'+sitename+datestr)
                    data = response.text
                    datalist= np.array(data.split('\r\n'))

                    for i in range(len(datalist)): 

                        linestr = datalist[i]
                        linesplit = linestr.split(',')

                        #print(len(linestr))

                        if 'CRC' in linestr and 'DATE' in linestr: ##check if the transmitted line contains all of the data and is not partial

                            try:

                                df.loc[i+dateiter] = [linesplit[linesplit.index('DATE')+1] if 'DATE' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('CO')+1]) if 'CO' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('SO2')+1]) if 'SO2' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('NO2')+1]) if 'NO2' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('O3')+1]) if 'O3' in linestr else np.NAN,
                                            int(linesplit[linesplit.index('CO2')+1]) if 'CO2' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('T')+1]) if 'T' in linestr else np.NAN,
                                            float(linesplit[linesplit.index('RH')+1]) if 'RH' in linestr else np.NAN,
                                            #float(linesplit[linesplit.index('MET')+1]) if 'MET' in linestr else np.NAN and if linesplit[linesplit.index('MET')+1].isdigit() in linestr]
                                            float(linesplit[linesplit.index('MET')+1]) if 'MET' in linestr else np.NAN] #if linesplit[linesplit.index('MET')+1].isnumeric() and
                            
                            except:
                                df.loc[i+dateiter] = [np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN, np.NAN]
                
                    dateiter = len(df.index)
                     
                        
        df.to_csv('RAMP_'+argv[1]+'_'+str(startdate)+'_'+str(enddate)+'.csv')                      

    else: ##if site number doesn't exist then exit script
            print('site number does not exist on server')
            return



# ---------------------------------------------------------------------------
def main():
    ##To add: mirror and download CCMz data
    # loop_over_flights_and_instruments()
    print('go')

    

if __name__ == "__main__": 
  # calling main function 
  RAMPDownload(sys.argv[:])

