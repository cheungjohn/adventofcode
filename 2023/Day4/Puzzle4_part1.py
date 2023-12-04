import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');
lines = input.readlines()
counter = 0
for line in lines:    
    line = line.strip()
    print(line)
    card_game = line.split(':')[1]    
    win_numbers = card_game.split('|')[0].strip().split()
    win_numbers = [int(i.strip()) for i in win_numbers]
    my_numbers = card_game.split('|')[1].strip().split()
    my_numbers = [int(i.strip()) for i in my_numbers]
    matches = 0
    for x in my_numbers:
        if x in win_numbers:
            matches += 1
    if matches != 0:        
        counter += pow(2, matches - 1)
print(counter)

