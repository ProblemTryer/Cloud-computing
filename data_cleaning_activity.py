import pandas as pd
import os
import re
import numpy as np
import sys
from matplotlib import pyplot as plt

activity = ['Activity_1.xlsx', 'Activity_2.xlsx']
columns = ['cow_id', 'activity', 'model', 'observation_time', 'server_time', 'local_id']

def data_cleaning(file_dict, f_name, save):
    df = pd.read_excel(file_dict + f_name, index_col=0, engine='openpyxl')
    size = len(df)
    df = df.drop(labels=['id', 'cow_id'])
    df = df.dropna(subset=['activity'])
    print(f'Clean file {f_name}, size={len(df)}, original size={size}')
    plt.title(f_name)
    df[['activity']].plot.hist(bins=50)
    plt.savefig(file_dict + './pic/' + f_name + '.jpg')
    if save:
        df.to_csv(file_dict + '/project_clean/')



if __name__ == '__main__':
    file_dict = "E:/Cloud Computing"
    save = False
    if len(sys.argv) > 1:
        file_dict = sys.argv[1]
    if len(sys.argv) > 2:
        save = sys.argv[2]
    file_dict = file_dict + '/Project_4/'
    for f_name in activity:
        data_cleaning(file_dict, f_name, save)