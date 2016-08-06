############################################################
#Author: Ryan Kallicharran                                 #
# Purpose: clean the data and index semester per student   #
# Date: 7/29/2016                                          #                                          
############################################################


import pandas as pd
import numpy as np


def label_race (rowx, rowy):
    if rowx != np.nan and rowy != np.nan:
        return max(rowx,rowy)
    if rowx != np.nan:
        return rowx
    return rowy

#fill dataframe from csv
df = pd.read_csv('all_data54.csv')#inpute file name here
df['admission_sc'] = np.nan
df['start_dt'] = pd.to_datetime(df.start_dt)
df = df.sort_values(by=['studentid','start_dt'],ascending=[True, True])
df2 = df.groupby(['studentid', 'start_dt'], as_index=False,)['grade_num'].mean()
df_uniqueid = df.drop_duplicates('studentid')
df3 = pd.merge(df2, df_uniqueid, on='studentid', how='left')
df3['admission_sc'] = df3.apply(lambda x: label_race(x['trans_caa'], x['caa']), axis=1)
mean_dist = df3['admission_sc'].mean()
df3['admission_sc'].replace(np.nan,mean_dist,inplace=True)

Count_Row=df3.shape[0] #gives number of row count
df3['semester'] = None

counts = dict()
counter = 0
for i, row in df3.iterrows():
    key = row['studentid']
    if counts.has_key(key):
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1
    counter= counter +1
    print counter,
    print 'of ',
    print Count_Row
    df3.loc[i, 'semester'] = counts[key]

#take only these columns of data
df4 = df3[['studentid','age', 'start_dt_x' , 'admission_sc','grade_num_x',
           'graduated_2005_2015', 'semester', 'admissiontypedesc']]


#write result to file
df4.to_csv('Final_DataSet_with_studentid_allzz.csv')#inpute a new file name that will be output
