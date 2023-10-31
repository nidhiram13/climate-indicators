#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request

Profilefolder = "Users/nidhiram/PGSS/Profiles2/"

Metafolder = "Users/nidhiram/PGSS/Indices2/"



##date parameters
startyear = 1990    
endyear = 2023
startmonth = 1
endmonth = 12

yearlist = [n for n in range(startyear, endyear+1)]
monthlist = [n for n in range(startmonth, endmonth+1)]
padded_list = [f"{x:0{2}}" for x in monthlist]


for year in range(len(yearlist)):

    for month in range(len(padded_list)):

        # print(str(yearlist[year]))
        # print(padded_list[month])
        page = urllib.request.urlopen('http://weather.uwyo.edu/cgi-bin/sounding?region=naconf&TYPE=TEXT%3ALIST&YEAR='+str(yearlist[year])+'&MONTH='+padded_list[month]+'&FROM=all&TO=3112&STNM=72520').read()
        soup = BeautifulSoup(page, 'html.parser')

        headertag = soup.find_all('h2')
        datatag = soup.find_all('pre')

        print(len(headertag))

        for header in range(len(headertag)):

         ##find file name
            headerstr = str(headertag[header]).replace(" ","<")
            modstr = headerstr.split("<")
            filestr = modstr[2]+'_'+modstr[9]+'_'+modstr[8]+'_'+modstr[7]+'_'+modstr[6]
   
            ##export profile data to text files
            datafile = open(Profilefolder+'Profile_'+filestr+'.csv','w')
            datafile.write(datatag[header*2].string)

            ##export indices data to text files
            metafile = open(Metafolder+'MetIndices_'+filestr+'.csv','w')
            metafile.write(datatag[(header*2)+1].string)




# ---------------------------------------------------------------------------
def main():

    print('load files')

if __name__ == "__main__": 
  # calling main function 
  main() 