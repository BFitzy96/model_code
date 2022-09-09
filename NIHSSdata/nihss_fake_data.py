# code to create fake data to train a model
import time
import numpy as np
import pandas as pd
import random


def unique(set):
    uniq_set = []
    for x in set:
        if x not in uniq_set:
            uniq_set.append(x)
    return uniq_set


df = pd.read_csv(
    '/home/brugha/Desktop/Project/NIHSSdata/NIHSSgen.csv', header=4)


def nihss_data_gen(df, n):

    df.dropna(axis=0, thresh=0.2, inplace=True)
    df.dropna(axis=1, thresh=0.2, inplace=True)
    df.drop(columns=['code'], inplace=True)
    # translate to english from polish
    columns = list(df.columns)
    # K is female, M is Male
    for i in range(len(df['sex'])):
        if df['sex'].iloc[i] == 'K':
            df['sex'].iloc[i] = 'F'

    catergoricalData = df.iloc[:, 7:11]
    df = df.drop(columns=catergoricalData.columns)

    sex = [i for i in catergoricalData['sex']]
    strokeHaem = [i for i in catergoricalData['strokehemorhage']]
    ant_post = [i for i in catergoricalData['anterior/posterior']]
    stroke_typ = [i for i in catergoricalData['storke typ']]

    uniq_sex = unique(sex)
    uniq_strokeHaem = unique(strokeHaem)
    uniq_ant_post = unique(ant_post)
    uniq_stroke_typ = unique(stroke_typ)

    df = df.join(catergoricalData)
    columns = list(df.columns)

    patient_lst = []
    row_lst = []
    for i in range(1, n+1):
        patient = 'patient' + str(i)
        patient_lst.append(patient)

    # this for loop creates random values based on the
    # min/max value of the columns

    for i in range(0, n):
        values = []
        for d in range(len(columns)):
            if df.iloc[:, d].dtype == np.float64:
                values.append(np.round(np.random.uniform(
                    min(df.iloc[:, d]), max(df.iloc[:, d]))))
            else:
                if columns[d] == 'sex':
                    values.append(random.choice(uniq_sex))
                elif columns[d] == 'strokehemorhage':
                    values.append(random.choice(strokeHaem))
                elif columns[d] == 'anterior/posterior':
                    values.append(random.choice(ant_post))
                elif columns[d] == 'storke typ':
                    values.append(random.choice(stroke_typ))
        for j in range(len(values)):
            curr = values[j]
            row_lst.append(curr)

    patient_values = []

    for i in range(0, len(row_lst), 19):
        patient_values.append(row_lst[i:i+19])

    fake_patient_dict = dict(zip(patient_lst, patient_values))

    # make a df from the dictionary
    final_df = pd.DataFrame.from_dict(
        fake_patient_dict, orient='index', columns=columns)

    # write df to csv file
    pd.DataFrame.to_csv(final_df, 'ficticious_data.csv')


start = time.time()

nihss_data_gen(df, 10000)

passed_time = time.time() - start

print(f'Time passed = {np.round(passed_time,2)} seconds')
