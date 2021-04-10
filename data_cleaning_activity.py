import pandas as pd
import os
import re
import numpy as np
import sys
from matplotlib import pyplot as plt

activity = [ 'Activity_2.xlsx']
columns = ['cow_id', 'activity', 'model', 'observation_time', 'server_time', 'local_id']

def data_cleaning(file_dict, f_name, save):
    df = pd.read_excel(file_dict + f_name, index_col=0, engine='openpyxl')
    size = len(df)
    df['activity'] = df[df['activity'] < 1000]
    df.dropna(subset=['activity'], inplace=True)
    print(f'Clean file {f_name}, size={len(df)}, original size={size}')
    plt.title(f_name)
    df[['activity']].plot.box()
    plt.savefig('./pic/' + f_name.replace('.xlsx', '_cl') + '.jpg')
    plt.show()
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