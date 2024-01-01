import pandas as pd

dataset_folder_path = 'Dataset/'
def read_data(x):
    df = pd.read_csv(f'{dataset_folder_path}{x}')
    return df


