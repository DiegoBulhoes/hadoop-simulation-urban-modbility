#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
from operator import add

currently_vehicle = None
currently_data = list(0 for i in range(13))

for line in sys.stdin:
    input = line.replace('\n', '').split(';')
    data = [float(i) for i in input[1:11]]
    vehicle_name = input[-1]
    if vehicle_name == currently_vehicle:
        currently_data = list(map(add, currently_data, data))
    else:
        if currently_vehicle:
            print('{0};{1}'.format(currently_vehicle, currently_data))
        currently_vehicle = vehicle_name
        currently_data = data

if currently_vehicle == vehicle_name:
    print('{0};{1}'.format(currently_vehicle, currently_data))
