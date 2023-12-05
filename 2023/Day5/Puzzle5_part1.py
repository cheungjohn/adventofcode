import os

def get_file_as_list(file_name):
    absolute_path = os.path.dirname(os.path.abspath(__file__))
    file_path = absolute_path + '\\' + file_name
    input = open(file_path, 'r');    
    data = input.read()
    return data

def construct_map(maps):
    map_list = []
    for map_text in maps:
        map = []
        map_elements = map_text.split('\n')
        for line in map_elements[1:]:
            numbers = line.split()
            map.append((int(numbers[0]), int(numbers[1]), int(numbers[2])))
        map_list.append(map)
        print(map)
    return map_list

def get_seeds(line):
    seeds = []
    split_line = line.split()
    for seed in split_line[1:]:
        seeds.append(int(seed))
    return seeds

def get_map_translated_value(seed, maps):
    map = maps[0]
    new_seed = -1
    for interval in map:        
        if interval[1] <= seed and seed <= (interval[1] + interval[2] - 1):
            new_seed = interval[0] + (seed - interval[1])
            break
    if new_seed == -1:
        new_seed = seed;
    if len(maps) == 1:
        return new_seed
    else:
        return get_map_translated_value(new_seed, maps[1:])

locations = []
lines = get_file_as_list('input.txt')
array = lines.split('\n\n')
seeds = get_seeds(array[0])
maps = construct_map(array[1:])
for seed in seeds:
    locations.append(get_map_translated_value(seed, maps))
print(locations)
print(min(locations))



    

