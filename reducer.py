#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
from operator import add

qty_vehicle = 1
currently_vehicle = None
currently_data = list(0 for i in range(10))
currently_data_min = list((float('inf')) for i in range(10))
currently_data_max = list((float('-inf')) for i in range(10))


def output_reducer(currently_data, currently_vehicle, currently_data_max, currently_data_min, mean):
    str_currently_data = ';'.join(map(str, currently_data))
    str_currently_data_max = ';'.join(map(str, currently_data_max))
    str_currently_data_min = ';'.join(map(str, currently_data_min))
    str_mean = ';'.join(map(str, mean))
    return f'{currently_vehicle};{str_currently_data};{str_currently_data_max};{str_currently_data_min};{str_mean}'


def parse_input(input_func_reducer):
    input = input_func_reducer.replace('\n', '').split(';')
    data = [float(i) for i in input[2:-1]]
    vehicle_name = input[-1]
    return vehicle_name, data

for input_func_reducer in sys.stdin:
    vehicle_name, data = parse_input(input_func_reducer)
    if vehicle_name == currently_vehicle:
        currently_data = list(map(add, currently_data, data))
        currently_data_max = [l1 if l1 > l2 else l2 for l1, l2 in zip(currently_data_max, data)]
        currently_data_min = [l1 if l1 < l2 else l2 for l1, l2 in zip(currently_data_min, data)]
        qty_vehicle += 1
    else:
        if currently_vehicle:
            mean = list(map(lambda x: x / qty_vehicle, currently_data))
            print(output_reducer(currently_data, currently_vehicle, currently_data_max, currently_data_min, mean))
        currently_vehicle = vehicle_name
        currently_data = data

if currently_vehicle == vehicle_name:
    mean = list(map(lambda x: x / qty_vehicle, currently_data))
    print(output_reducer(currently_data, currently_vehicle, currently_data_max, currently_data_min, mean))
