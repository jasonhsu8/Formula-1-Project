import pandas as pd

# Read csv Data fron specific folder function
dataset_folder_path = 'Dataset/'
def read_data(x):
    df = pd.read_csv(f'{dataset_folder_path}{x}')
    return df


# Count number of DNFs function
def dnf_count(results_df, race_id_in_results):
    #counter for DNFs
    dnf_counter = 0
    #Array for each statusId that a driver finsihed the race in status.csv
    status_finished_race = [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 45, 50, 128, 53, 55, 58, 88, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 127, 133, 134]

    for i in results_df[results_df['raceId'] == race_id_in_results]['statusId']:
        if i not in status_finished_race:
            dnf_counter = dnf_counter + 1
        else:
            pass

    return dnf_counter