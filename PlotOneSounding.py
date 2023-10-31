
import os
import sys
import urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


cwd = os.getcwd()
if not os.path.isdir("/Users/nidhiram/PGSS/Profiles"): ##make path for profile files
   print()
Profilefolder = "/Users/nidhiram/PGSS/Profiles"


def PlotSingle(argv):

   # print ('Profilefolder/'+argv[1])
    colnames =['Pressure','Height','Temperature','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
    profile = pd.read_fwf(Profilefolder+'/'+argv[1],  skiprows=5, header = 0, names = colnames)
    #print (dataframe)

    profile.plot.line(x='Temperature',y='Height')
    plt.show()

    
if __name__ == "__main__": 
  # calling main function 
  PlotSingle(sys.argv[:])