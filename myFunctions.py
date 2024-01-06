import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# Coefficients for Linear Regression
# This gets the y intercept and the gradient
def coef_linear_regression(x,y):
    n = np.size(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    ss_xy = np.sum(y*x) - n*y_mean*x_mean
    ss_xx = np.sum(x*x) - n*x_mean*x_mean

    gradient = ss_xy / ss_xx
    y_intercept = y_mean - gradient*x_mean

    return(y_intercept, gradient)


# Calculates the pearson correlation coeffiecient
def correlation_coefficient(x,y):

    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    x_denominator = np.sum((x - x_mean)**2)
    y_denominator = np.sum((y - y_mean)**2)
    denominator = np.sqrt(x_denominator * y_denominator)

    corr_coef = numerator / denominator

    return corr_coef

# Plots the linear regression line on a scatter plot
def plot_regression_line(x,y,b):
    plt.scatter(x, y, color='m', marker="o", s=30)

    y_pred = b[0]+b[1]*x
    plt.plot(x, y_pred, color="g")
    plt.show()

# overtaking_count function
# For something to count as an "overtake", a driver changes their position between two consecutive laps. This would mean an "overtake" has occured.
# Count this number then divide by 2 will give the number of overtakes as one overtake includes one driver gaining a position and the other losing a position.
def overtaking_count(laptimes, race_id):
    drivers = []
    for driver in laptimes[laptimes.raceId == race_id].driverId:
        if driver not in drivers:
            drivers.append(driver)
    
    prev_pos = 0
    overtakes = 0
    for driver in drivers:
        for lapPos in laptimes[(laptimes.raceId == race_id) & (laptimes.driverId == driver)].position:
            if lapPos != prev_pos:
                prev_pos = lapPos
                overtakes = overtakes + 1
                overtakings = overtakes/2
                
    return int(overtakings)