-# Ficticious data generator for Machine Learning
# Author Brugha Fitzpatrick
# Date of 1.0.0 creation: 2022/05/23


import numpy as np
import pandas as pd
import pandas.api.types as pda

file = input('Enter the path for the csv file: ')
no_of_fake_pats = input('How many patients?: ')

df = pd.read_csv(file, skipinitialspace=True, na_values='?')


def fake_results_gen(df, n):
    all_cols = list(df.columns)
    n = int(n)

    # look through df to find which is the first column
    # that contains numbers
    for l in all_cols:
        if df[l].dtype == np.number:
            indx = all_cols.index(l)
            break

    # sets the df to only contain the number values
    df = df.iloc[:, indx:]
    columns = list(df.columns)
    # ensure that all values are floats, if not ignore them
    # but will be addressed later
    df = df.astype(dtype=np.float64, errors='ignore')
    # drop the NaN values from the df
    df = df.dropna(axis=1, thresh = 0.2)
    patient_lst = []
    row_lst = []

    # checks if there are object types in the df and
    # converts to strings
    for m in columns:
        if pda.is_object_dtype(df[m]) == True:
            df[m] = df[m].convert_dtypes()

    # the converted objects are then converted to numerics
    for k in columns:
        if pda.is_string_dtype(df[k]) == True:
            df[k] = df[k].apply(lambda x: float(x.split()[0].replace(',', '')))

    for i in range(1, n+1):
        patient = 'patient' + str(i)
        patient_lst.append(patient)

    # this for loop creates random values based on the
    # min/max value of the columns
    for d in columns:
        values = [np.random.uniform(min(df[d]), max(df[d]))
                  for i in range(1, n+1)]
        for j in range(len(values)):
            curr = values[j]
            row_lst.append(curr)

    patient_values = []
    for p in range(0, n):
        pat = []
        q = 0
        for f in range(0, len(columns)):
            pat.append(row_lst[q+p])
            q += n

        patient_values.append(pat)

    fake_patient_dict = dict(zip(patient_lst, patient_values))

    # make a df from the dictionary
    final_df = pd.DataFrame.from_dict(
        fake_patient_dict, orient='index', columns=columns)

    # write df to csv file
    pd.DataFrame.to_csv(final_df, 'ficticious_data.csv')


fake_results_gen(df, no_of_fake_pats)
