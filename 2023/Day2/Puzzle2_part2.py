import os
import re

color_map = { 'red': 12,
             'green': 13,
             'blue': 14}

def get_int_from_string(text_string):
    number_string = ''.join(c for c in text_string if c.isdigit())
    return int(number_string)

def is_cube_list_possible(cube_list):
    for cube in cube_list:
        cube = cube.strip()        
        cube_split = cube.split(' ')
        if int(cube_split[0]) > color_map[cube_split[1]]:
            return False
    return True

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');

counter = 0
for line in input:
    line = line.strip()
    print(line)
    cube_string = line.split(':')[1]
    cube_list = re.split('; |,',cube_string)
    if is_cube_list_possible(cube_list):
        id_string = line.split(':')[0]
        id = get_int_from_string(id_string)
        counter += id
        print(id)
print(counter)