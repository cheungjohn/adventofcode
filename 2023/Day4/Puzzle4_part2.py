import os

def get_matches(line):
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
    return matches

absolute_path = os.path.dirname(os.path.abspath(__file__))
file_path = absolute_path + '\\input.txt'
input = open(file_path, 'r');
lines = input.readlines()
cards = [1] * len(lines)
for idx, line in enumerate(lines):    
    matches = get_matches(line)
    for x in range(1, matches + 1):
        cards[idx + x] = cards[idx + x] + cards[idx]
print(cards)
print(sum(cards))