import csv
import matplotlib.pyplot as plt
import matplotlib
import time

def read_csv(file_name):
    file = open(file_name)
    file_data = csv.reader(file)
    return file_data 

def get_time():
    file_data = read_csv('sensor_data_with_noize_6000_samples.csv')
    time_data = []
    for columns in file_data:
        time_data.append(columns[0])
    return time_data
    
def get_encoder_position():
    file_data = read_csv('sensor_data_with_noize_6000_samples.csv')
    encoder_position_data = []
    for columns in file_data:
        encoder_position_data.append(columns[1])
    return encoder_position_data

def get_integral(pre_integrated_value,x2,x3,y2,y3):
    integrated_value = pre_integrated_value + (y3+y2)*(x3-x2)/2
    return [pre_integrated_value,integrated_value]
    
def data_integrating():
    time_data = get_time()
    encoder_position_data = get_encoder_position()
    filtered_encoder_position_data = [0]
    pre_integrated_value = 0
    y=0
    g=0.2
    for i in range(0,len(encoder_position_data)-1):
        y=g*filter_integration(pre_integrated_value,float(time_data[i]),float(time_data[i+1]),y)
        pre_integrated_value=y/g
        filtered_encoder_position_data.append(y)
    return filtered_encoder_position_data

def filter_integration(pre_integrated_value,x1,x2,y):
    y = pre_integrated_value+ (x1-y)*(x2-x1)
    return y


def plot_data(x,y):   
    plt.ylim(min(y), max(y))
    plt.scatter(x, y)
    plt.show()



filtered_data = data_integrating()
time_data = get_time()
plot_data(time_data,get_encoder_position())
input()
