import os

def get_num_and_index_list(str):
    lst = []
    buildstring = ''
    for idx, c in enumerate(str):
        if c.isdigit():
            buildstring += c
        else:
            if buildstring:                
                lst.append([buildstring, idx - len(buildstring)])
                buildstring = ''
    if buildstring:                
        lst.append([buildstring, idx - len(buildstring)])
    return lst

def get_int_from_string(text_string):
    number_string = ''.join(c for c in text_string if c.isdigit())
    return int(number_string)

def get_symbol_index_list(line_string):
    return [i for i, letter in enumerate(line_string) if (not letter.isalnum() and letter != '.')]

def has_symbol(line_string):
    for letter in line_string:
        if not letter.isalnum() and letter != '.':
            return True
    return False

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
    num_list = get_num_and_index_list(line)
    if len(num_list) == 0:
        continue
    for num_pair in num_list:
        print('Number: ' + num_pair[0] + ' at index ' + str(num_pair[1]))
        start_index = num_pair[1] - 1        
        if start_index < 0:
            start_index = 0
        end_index = num_pair[1] + len(num_pair[0])
        if end_index >= len(line):
            end_index = len(line) - 1        
        if has_symbol(line[start_index:end_index + 1]):
            counter += int(num_pair[0])
        if has_symbol(previous_line[start_index:end_index + 1]):
            counter += int(num_pair[0])        
        if has_symbol(next_line[start_index:end_index + 1]):
            counter += int(num_pair[0])
        print('Counter: ' + str(counter))
print(counter)