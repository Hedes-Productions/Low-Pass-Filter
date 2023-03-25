import csv
import matplotlib.pyplot as plt

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

def convert_scientific_notation_to_float(list_of_data):
    list_of_float_data = []
    for data in list_of_data:
        list_of_float_data.append((float(data)))
    return list_of_float_data
    
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
    g=450
    for i in range(0,len(encoder_position_data)-1):
        y=g*filter_integration(pre_integrated_value,float(encoder_position_data[i]),float(time_data[i]),float(time_data[i+1]),y)
        pre_integrated_value=y/g
        filtered_encoder_position_data.append(y)
    return filtered_encoder_position_data

def filter_integration(pre_integrated_value,y1,t1,t2,y):
    y = pre_integrated_value+ (y1-y)*(t2-t1)
    return y

def plot_data(time,filtered_y, original_y):   
    plt.subplot(211)
    plt.plot(time, original_y)
    plt.subplot(212)
    plt.plot(time, filtered_y)
    plt.show()
    
filtered_y = convert_scientific_notation_to_float(data_integrating())
time = convert_scientific_notation_to_float(get_time())
original_y = convert_scientific_notation_to_float(get_encoder_position())
plot_data(time,filtered_y, original_y)
