import pandas as pd
import datetime
import numpy as np
import time
columns = ['Settlement Date','Settlement Period','Biomass','Hydro Pumped Storage','Hydro Run-of-river and poundage','Fossil Hard coal',
'Fossil Gas','Fossil Oil','Nuclear','Other','Wind Onshore','Wind Offshore','Solar']


df = pd.read_csv('Generation.csv', skiprows = 4)
df = df.dropna().reset_index()
df_new = pd.DataFrame()

time_0 = time.time()
counter = 0
while counter < len(df):
    if df.iloc[counter][2] != "Business Type":
        row_list = []
        row_list.append(df[columns[0]][counter])
        row_list.append(int(df[columns[1]][counter]))
        for val in range(11):
            row_list.append(float(df['Quantity'][counter+val]))
            
        df_temp = pd.DataFrame([row_list], columns = columns)
        df_new = df_new.append(df_temp)
        counter = counter + 11
        print(counter)
    else:
        counter = counter + 1
        print(counter)
    

# =============================================================================
# time_0 = time.time()
# counter = 0
# while counter < len(df):
#     row_list = []
#     if counter%533 not in [528,529,530,531,532]: 
#         row_list.append(df[columns[0]][counter])
#         row_list.append(int(df[columns[1]][counter]))
#         for val in range(11):
#             row_list.append(float(df['Quantity'][counter+val]))
#             
#         df_temp = pd.DataFrame([row_list], columns = columns)
#         df_new = df_new.append(df_temp)
#         counter = counter + 11
#         print(counter)
#     else:
#         counter = counter + 5
#         print(counter)
# 
# =============================================================================
    







# =============================================================================
# with open('Generation.csv', 'r') as file:
#     counter = 0
#     N = 0
#     for line in file:
#         counter += 1
#         if counter < 6 + N:
#             continue
#         split_lines = line.split(',')
#         #data_list = []
#         #for val in columns[]:
#         quant = int(split_lines[4])
#         date = pd.to_datetime(split_lines[7])
#         period = int(split_lines[8])
#         df.
#         break
#         
#         
#         
#         
#         
# =============================================================================
        
