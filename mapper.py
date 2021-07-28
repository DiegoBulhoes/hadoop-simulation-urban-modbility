#!/usr/bin/python3
# -*-coding:utf-8 -*
import sys

def remove(dictionary_input, list_keys=None):
    if list_keys is None:
        list_keys = ['vehicle_angle', 'vehicle_id', 'vehicle_lane', 'vehicle_pos', 'vehicle_route', 'vehicle_waiting',
                     'vehicle_x', 'vehicle_y', 'vehicle_eclass']
    for key in list_keys:
        dictionary_input.pop(key)
    return dictionary_input


def parse_input(input_mapper):
    keys = ['timestep_time', 'vehicle_CO', 'vehicle_CO2', 'vehicle_HC', 'vehicle_NOx', 'vehicle_PMx', 'vehicle_angle',
            'vehicle_eclass', 'vehicle_electricity', 'vehicle_fuel', 'vehicle_id', 'vehicle_lane', 'vehicle_noise',
            'vehicle_pos', 'vehicle_route', 'vehicle_speed', 'vehicle_type', 'vehicle_waiting', 'vehicle_x',
            'vehicle_y']
    words = input_mapper.split(';')
    processed_input = remove(dict(zip(keys, words)))
    return processed_input


for input_mapper in sys.stdin:
    processed_input = parse_input(input_mapper)
    data = list(processed_input.values())
    vehicle = ['moto_motorcycle', 'bus_bus', 'veh_passenger', 'truck_truck']
    if data[1] != "0.00" and processed_input['vehicle_type'] in vehicle:
        print('{};{}'.format(processed_input['vehicle_type'], ';'.join(data).replace('\n', '')))
