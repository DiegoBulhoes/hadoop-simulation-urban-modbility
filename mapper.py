#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys
import os


def remove(dict_input,
           list_keys=['vehicle_angle', 'vehicle_id', 'vehicle_lane', 'vehicle_pos', 'vehicle_route', 'vehicle_waiting',
                      'vehicle_x', 'vehicle_y', 'vehicle_eclass']):
    for l in list_keys:
        dict_input.pop(l)
    return dict_input


def parse_input(line):
    keys = ['timestep_time', 'vehicle_CO', 'vehicle_CO2', 'vehicle_HC', 'vehicle_NOx', 'vehicle_PMx', 'vehicle_angle',
            'vehicle_eclass', 'vehicle_electricity', 'vehicle_fuel', 'vehicle_id', 'vehicle_lane', 'vehicle_noise',
            'vehicle_pos', 'vehicle_route', 'vehicle_speed', 'vehicle_type', 'vehicle_waiting', 'vehicle_x',
            'vehicle_y']
    words = line.split(';')
    return keys, words


for line in sys.stdin:
    word = line.split()
    keys, words = parse_input(line)
    dict_input = dict(zip(keys, words))
    dict_processed_input = remove(dict_input)
    data = list(dict_processed_input.values())
    vehicle = ['moto_motorcycle', 'bus_bus', 'veh_passenger', 'truck_truck']
    if data[1] != "" and dict_processed_input['vehicle_type'] in vehicle:
        print('{};{}'.format(dict_processed_input['vehicle_type'], ';'.join(data).replace('\n', '')))
