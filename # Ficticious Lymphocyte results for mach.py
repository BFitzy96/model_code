# Ficticious Lymphocyte results for machine learning project
# ApoE data
import csv
from fileinput import close
import numpy
import random
import pandas as pd

df = pd.read_csv('/home/brugha/Documents/Project/ApoE DB.csv', header=2
                 )


def fake_results_gen(df, n):
    patient_lst = []
    row_lst = []
    for i in range(1, n+1):
        patient = 'patient' + str(i)
        patient_lst.append(patient)
    cd3_spleen = [random.uniform(min(df['CD3']), max(df['CD3']))
                  for i in range(1, n+1)]
    cd4_spleen = [random.uniform(min(df['CD4']), max(df['CD4']))
                  for i in range(1, n+1)]
    cd8_spleen = [random.uniform(min(df['CD8']), max(df['CD8']))
                  for i in range(1, n+1)]
    cd25_spleen = [random.uniform(min(df['CD25']), max(df['CD25']))
                   for i in range(1, n+1)]
    foxp3_spleen = [random.uniform(min(df['FOXP3']), max(df['FOXP3']))
                    for i in range(1, n+1)]
    Treg_spleen = [random.uniform(min(df['Treg']), max(df['Treg']))
                   for i in range(1, n+1)]
    cd3_cln = [random.uniform(min(df['CD3-2']), max(df['CD3-2']))
               for i in range(1, n+1)]
    cd4_cln = [random.uniform(min(df['CD4-2']), max(df['CD4-2']))
               for i in range(1, n+1)]
    cd8_cln = [random.uniform(min(df['CD8-2']), max(df['CD8-2']))
               for i in range(1, n+1)]
    cd25_cln = [random.uniform(min(df['CD25-2']), max(df['CD25-2']))
                for i in range(1, n+1)]
    foxp3_cln = [random.uniform(min(df['FOXP3-2']), max(df['FOXP3-2']))
                 for i in range(1, n+1)]
    Treg_cln = [random.uniform(min(df['Treg-2']), max(df['Treg-2']))
                for i in range(1, n+1)]
    cd3_iln = [random.uniform(min(df['CD3-3']), max(df['CD3-3']))
               for i in range(1, n+1)]
    cd4_iln = [random.uniform(min(df['CD4-3']), max(df['CD4-3']))
               for i in range(1, n+1)]
    cd8_iln = [random.uniform(min(df['CD8-3']), max(df['CD8-3']))
               for i in range(1, n+1)]
    cd25_iln = [random.uniform(min(df['CD25-3']), max(df['CD25-3']))
                for i in range(1, n+1)]
    foxp3_iln = [random.uniform(min(df['FOXP3-3']), max(df['FOXP3-3']))
                 for i in range(1, n+1)]
    Treg_iln = [random.uniform(min(df['Treg-3']), max(df['Treg-3']))
                for i in range(1, n+1)]
    cd3_blood = [random.uniform(min(df['CD3-4']), max(df['CD3-4']))
                 for i in range(1, n+1)]
    cd4_blood = [random.uniform(min(df['CD4-4']), max(df['CD4-4']))
                 for i in range(1, n+1)]
    cd8_blood = [random.uniform(min(df['CD8-4']), max(df['CD8-4']))
                 for i in range(1, n+1)]
    cd25_blood = [random.uniform(min(df['CD25-4']), max(df['CD25-4']))
                  for i in range(1, n+1)]
    foxp3_blood = [random.uniform(min(df['FOXP3-4']), max(df['FOXP3-4']))
                   for i in range(1, n+1)]
    Treg_blood = [random.uniform(min(df['Treg-4']), max(df['Treg-4']))
                  for i in range(1, n+1)]

    columns = ['patients', 'cd3_spleen', 'cd4_spleen', 'cd8_spleen',
               'cd25_spleen', 'foxp3_spleen', 'Treg_spleen',
               'cd3_cln', 'cd4_cln', 'cd8_cln', 'cd25_cln', 'foxp3_cln',
               'Treg_cln', 'cd3_iln', 'cd4_iln', 'cd8_iln', 'cd25_iln',
               'foxp3_iln', 'Treg_iln', 'cd3_blood', 'cd4_blood',
               'cd8_blood', 'cd25_blood', 'foxp3_blood', 'Treg_blood']

    for k in range(len(cd3_spleen)):
        curr = [cd3_spleen[k], cd4_spleen[k], cd8_spleen[k],
                cd25_spleen[k], foxp3_spleen[k], Treg_spleen[k],
                cd3_cln[k], cd4_cln[k], cd8_cln[k], cd25_cln[k], foxp3_cln[k],
                Treg_cln[k], cd3_iln[k], cd4_iln[k], cd8_iln[k], cd25_iln[k],
                foxp3_iln[k], Treg_iln[k], cd3_blood[k], cd4_blood[k],
                cd8_blood[k], cd25_blood[k], foxp3_blood[k], Treg_blood[k]]
        row_lst.append(curr)
    fake_patient_dict = dict(zip(patient_lst, row_lst))

    # To write the data to a csv file for future access
    try:
        with open('ficticious_data.csv', 'w', newline='') as f:
            content = csv.writer(f)
            content.writerow(columns)
            for pats, data in fake_patient_dict.items():
                content.writerow(
                    [pats, data[0], data[1], data[2], data[3], data[4], data[5], data[6],
                     data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14],
                     data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22]])
            f.close()
    except IOError:
        print('I/O Error')


fake_results_gen(df, 100)
