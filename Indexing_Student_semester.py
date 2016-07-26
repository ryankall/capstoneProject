import pandas as pd

#Indexed the number of semester a student took


#fill dataframe from csv
df = pd.read_csv('Final_DataSet_with_studentid.csv')#inpute file name here 
df['semester'] = None
counts = dict()
for i, row in df.iterrows():
    key = row['studentid']
    if counts.has_key(key):
        counts[key] = counts[key] + 1
    else:
        counts[key] = 1

    df.loc[i, 'semester'] = counts[key]

#take only these columns of data
df = df[['studentid','age', 'admission_sc','semester_gpa', 'semester']]

#write result to file
df.to_csv('Final_DataSet_with_studentid_allx.csv')#inpute a new file name that will be output
