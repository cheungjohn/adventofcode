# Part 1
def get_coordinate_from_string(coordinateString):
    numberString = ''.join(c for c in coordinateString if c.isdigit())
    return int(numberString[0] + numberString[len(numberString) - 1])

totalCoordinate = 0;
counter = 0;
input = open('input.txt', 'r');
for line in input:
    counter += 1;
    coordinate = get_coordinate_from_string(line);
    print("Line " + str(counter) + ": " + str(coordinate));
    totalCoordinate += coordinate;
print(totalCoordinate);