import os

directory = "/Users/nidhiram/PGSS/Indices"
for file in os.listdir(directory):
    if file.endswith('.txt'):
        with open(os.path.join(directory, file)) as f:
            for line in f:
                if line.startswith("      Convective Available Potential Energy"):
                    with open("cape.txt1", "a") as cape:
                        cape_value = float(line.split(':')[1].strip())
                        if cape_value != float(0.0):
                            cape.write(str(cape_value) + "\n")

# import os
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from datetime import datetime
# import csv

# directory = "/Users/nidhiram/PGSS/Profiles"
# colnames =['Pressure','Height','Temperature','DewPoint','RH','MIXR', 'WD', 'WS', 'ThetaA', 'ThetaE', 'ThetaV']
# for filepath in os.listdir(directory):
#     file = os.path.join(directory, filepath)
#     if os.path.isfile(file):
#         with open(file, "r") as f:
#             df = pd.read_fwf(f, skiprows=5, names = colnames)
#             df['dT'] = df['Temperature'].diff()
#             df['dZ'] = df['Height'].diff()
#             df['dZ'] = df['dZ']/1000
#             df['dT/dZ'] = df['dT']/df['dZ']
#             df['dT/dZ'] = -1 * df['dT/dZ']
#             for i in df.index:
#                 if df.loc[i, 'Height'] >= float(5000) and df.loc[i, 'dT/dZ'] <= 2.00:
#                     with open("lapserate2.csv", "a") as l:
                        
#                         l.write(file + "\n" + str(df['Height'][i])+ ": " + str(df['dT/dZ'][i]) + "\n")
#                     break
#                 else:
#                     continue