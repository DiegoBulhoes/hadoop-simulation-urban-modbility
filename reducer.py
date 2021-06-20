#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
from operator import add

currently_vehicle = None
currently_data = list(0 for i in range(13))
currently_data_min = list((float('inf')) for i in range(13))
currently_data_max = list((float('-inf')) for i in range(13))

qtd = 0
max = (float('-inf'))
min = (float('inf'))


def output_reducer(currently_data, currently_vehicle, mean):
    str_currently_data = ';'.join(map(str, currently_data))
    str_mean = ';'.join(map(str, mean))
    return f'{currently_vehicle};{str_currently_data};{str_mean}'


for line in sys.stdin:
    input = line.replace('\n', '').split(';')
    data = [float(i) for i in input[1:11]]
    vehicle_name = input[-1]
    if vehicle_name == currently_vehicle:
        currently_data = list(map(add, currently_data, data))
        currently_data_max = [n if n < m else m for n, m in zip(currently_data_max, data)]
        currently_data_min = [n if n > m else m for n, m in zip(currently_data_max, data)]
        qtd += 1
    else:
        if currently_vehicle:
            mean = list(map(lambda x: x / qtd, currently_data))
            print(output_reducer(currently_data, currently_vehicle, mean))
        currently_vehicle = vehicle_name
        currently_data = data

if currently_vehicle == vehicle_name:
    mean = list(map(lambda x: x / qtd, currently_data))
    print(output_reducer(currently_data, currently_vehicle, mean))
