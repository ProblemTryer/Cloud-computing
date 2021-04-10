import os
import pandas as pd
import re
import numpy as np
import sys
from matplotlib import pyplot as plt
import random


def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if str.isdigit(os.path.splitext(file)[0]):
                L.append(os.path.join(root, file))
    return L


def data_cleaning(file_dict, save):
    sensor_data_file = file_name(file_dict)
    ids = []
    for name in sensor_data_file:
        ids.append(int(name.replace(file_dict, '').replace('.csv', '')))

    cow_id_show = random.sample(ids, 3)
    print("Sample cow id", cow_id_show)
    for file in sensor_data_file:
        cow_id = int(file.replace(file_dict, '').replace('.csv', ''))
        data = pd.read_csv(file)
        size = len(data)
        data = data.drop(["heat_index"], axis=1)
        for column in columns:
            data[column] = data[column].apply(lambda x: x if np.isreal(x) else np.nan)
        data = data.drop(columns=['temp_dec_index'], axis=1)
        data = data.dropna(subset=['temp_without_drink_cycles', 'animal_activity'])

        # drop data with empty item in a row
        if save and len(data) > 0:
            data.to_csv(file_dict + '/project_clean/' + file)
        if len(data) > 0:
            show_distribution(cow_id_show, cow_id, data)
        print(f'Clean file {file}, size={len(data)}, original size={size}')


# randomly sample 3 cows for data distribution
def show_distribution(id_arr, id, data):
    if id in id_arr:
        col = ['temp_without_drink_cycles', 'animal_activity', 'low_pass_over_activity', 'stomach_temp']
        for i, c in enumerate(col):
            title = 'Cow_' + str(id) + "_" + c
            plt.title(title)
            data[[c]].plot.hist(bins=30)
            plt.savefig('./pic/' + title + '.jpg')


columns = ["act_heat_index_smart",
           "act_heat_index",
           "animal_activity",
           "low_pass_over_activity",
           "percentile60_of_5day_temp",
           "temp_height_index",
           "temp_inc_index",
           "temp_without_drink_cycles",
           'stomach_temp',
           "CowID"]

if __name__ == '__main__':
    file_dict = "E:/Cloud Computing"
    save = False
    if len(sys.argv) > 1:
        file_dict = sys.argv[1]
    if len(sys.argv) > 2:
        save = sys.argv[2]
    file_dict = file_dict + '/Project_4/'
    data_cleaning(file_dict, save)
