# Part 2
import os
import sys

numbers_in_text = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def get_first_int_char_index(coordinateString):
    numberString = ''.join(c for c in coordinateString if c.isdigit())
    return coordinateString.find(numberString[0])

def get_last_int_char_index(coordinateString):
    numberString = ''.join(c for c in coordinateString if c.isdigit())
    return coordinateString.rfind(numberString[len(numberString) - 1])   

def get_first_text_number_index_and_number(coordinateString):    
    numbers_index = [-1] * 9
    for number_in_text in numbers_in_text:
        index = coordinateString.find(number_in_text)
        number = numbers_in_text.index(number_in_text)
        numbers_index[number] = index
    if numbers_index.count(-1) == 9:
        return ( str(0), 1000000000000 )
    text_number_index = min(i for i in numbers_index if i >= 0)
    return ( str(numbers_index.index(text_number_index) + 1), text_number_index )

def get_last_text_number_index_and_number(coordinateString):
    numbers_index = [-1] * 9
    for number_in_text in numbers_in_text:
        index = coordinateString.rfind(number_in_text)
        number = numbers_in_text.index(number_in_text)
        numbers_index[number] = index
    if numbers_index.count(-1) == 9:
        return ( str(0), -1 )
    textNumberIndex = max(numbers_index)  
    return ( str(numbers_index.index(textNumberIndex) + 1), textNumberIndex )

totalCoordinate = 0;
counter = 0;
absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');
for line in input:
    line = line.strip();
    counter += 1;
    extracted_number_string = "";
    if line.isdigit():
        extracted_number_string = line[0] + line[len(line)-1];
    elif line.isalpha():        
        extracted_number_string += get_first_text_number_index_and_number(line)[0]
        extracted_number_string += get_last_text_number_index_and_number(line)[0]        
    else:
        first_int_index = get_first_int_char_index(line)
        first_text_index = get_first_text_number_index_and_number(line)
        if first_int_index < first_text_index[1]:
            extracted_number_string += line[first_int_index]
        elif first_int_index > first_text_index[1]:
            extracted_number_string += first_text_index[0]
        last_int_index = get_last_int_char_index(line)
        last_text_index = get_last_text_number_index_and_number(line)
        if last_int_index > last_text_index[1]:
            extracted_number_string += line[last_int_index]
        elif last_int_index < last_text_index[1]:
            extracted_number_string += last_text_index[0]        
    coordinate = int(extracted_number_string);
    print("Line " + str(counter) + ": " + line);
    print("Line " + str(counter) + ": " + str(coordinate));
    totalCoordinate += coordinate;
print(totalCoordinate);