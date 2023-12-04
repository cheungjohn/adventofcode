import os

def get_num_and_index_list(str, y_idx):
    lst = []
    buildstring = ''
    for idx, c in enumerate(str):
        if c.isdigit():
            buildstring += c
        else:
            if buildstring:                
                lst.append([buildstring, (idx - len(buildstring), y_idx)])
                buildstring = ''
    if buildstring:                
        lst.append([buildstring, (idx - len(buildstring), y_idx)])
    return lst

def get_int_from_string(text_string):
    number_string = ''.join(c for c in text_string if c.isdigit())
    return int(number_string)

def get_symbol_index_list(line_string):
    return [(i,1) for i, letter in enumerate(line_string) if (letter == '*')]

def has_symbol(line_string):
    for letter in line_string:
        if not letter.isalnum() and letter != '.':
            return True
    return False

def get_coordinate_list(num, y_idx):
    lst = []
    start_index = num[1][0] - 1
    end_index = num[1][0] + len(num[0])
    coordinates = list(range(start_index, end_index + 1))
    lst.append((start_index, y_idx))
    lst.append((end_index, y_idx))
    lst.extend(list(zip(coordinates, [y_idx - 1] * len(coordinates))))
    lst.extend(list(zip(coordinates, [y_idx + 1] * len(coordinates))))
    return lst

def get_all_numbers(grid):
    num_list = []
    for y in range(0, len(grid)):
        num_info = get_num_and_index_list(grid[y], y)
        for num in num_info:
            num_list.append((num[0], get_coordinate_list(num, y)))
    return num_list

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');
lines = input.readlines()
counter = 0
previous_line = ''
next_line = ''
for idx,line in enumerate(lines):
    line = line.strip()
    if idx == 0:
        previous_line = '.' * len(line)
    else:
        previous_line = lines[idx - 1].strip()
    if idx == len(lines) - 1:
        next_line = '.' * len(line)
    else:
        next_line = lines[idx + 1].strip()
    grid = [previous_line, line, next_line]

    symbol_list = get_symbol_index_list(line)
    if len(symbol_list) == 0:
        continue
    for sym_idx in symbol_list:
        print('Symbol: ' + line[sym_idx[0]] + ' at index ' + str(sym_idx[0]))
        number_list = get_all_numbers(grid)
        adjacent_numbers = []
        for number in number_list:
            if sym_idx in number[1]:
                adjacent_numbers.append(number[0])
        if len(adjacent_numbers) == 2:
            counter += int(adjacent_numbers[0]) * int(adjacent_numbers[1])
            print('Adjacent numbers: ' + str(adjacent_numbers))               
print(counter)