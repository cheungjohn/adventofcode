import os
import re

color_map = { 'red': 12,
             'green': 13,
             'blue': 14}

def get_int_from_string(text_string):
    number_string = ''.join(c for c in text_string if c.isdigit())
    return int(number_string)

def find_power(cube_list):
    red_list = []
    green_list = []
    blue_list = []

    for cube in cube_list:
        cube = cube.strip()
        cube_split = cube.split(' ')
        if cube_split[1] == 'red':
            red_list.append(int(cube_split[0]))
        elif cube_split[1] == 'green':
            green_list.append(int(cube_split[0]))
        elif cube_split[1] == 'blue':
            blue_list.append(int(cube_split[0]))
    
    return max(red_list, default=0) * max(green_list, default=0) * max(blue_list, default=0)

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');

counter = 0
for line in input:
    line = line.strip()
    print(line)
    cube_string = line.split(':')[1]
    cube_list = re.split('; |,',cube_string)
    counter += find_power(cube_list)
print(counter)