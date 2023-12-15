with open("input.txt",'r') as f:     data = f.read()
data = data.split('\n')
data = [list(d) for d in data]

def move_north(matrix, y, x):
    for i in range(y):
        if (y-1) - i >= 0:
            if matrix[(y-1) - i][x] != '.':
                break
            else:
                matrix[(y-1) - i][x] = 'O'
                matrix[(y) - i][x] = '.'
    return matrix

def rotate(matrix):
    new_map = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[-1-j][i])
        new_map.append(new_row)
    return new_map

def move(matrix):
    new_board = matrix
    for y in range(len(new_board)):
        for x in range(len(new_board[y])):        
            point = new_board[y][x]
            if point == 'O':
                new_board = move_north(new_board, y, x)
    return new_board

def cycle(matrix):
    new_matrix = matrix
    for _ in range(4):
        new_matrix = move(new_matrix)
        new_matrix = rotate(new_matrix)
    return new_matrix


def print_map(data):
    for d in data:
        print(d)


def points(matrix):
    my_sum = 0
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O':
                my_sum+=length-i
    return my_sum

print(f"P1: {points(move(data))}")

def map_to_string(matrix):
    my_string = ""
    for x in matrix:
        my_string = my_string + ''.join(x)
    return my_string

new_map = data

repeating = set()
unique_map = set()
repeating_number = "yahoo"
repeating_length = 0

for i in range(1, 200):
    new_map = cycle(new_map)
    new_string = map_to_string(new_map)
    if new_string in unique_map:
        if repeating_number == "yahoo":
            repeating_number = i

        repeating.add(new_string)
        if repeating_length < len(repeating):
            repeating_length+=1

    unique_map.add(new_string)

number = repeating_number + (1_000_000_000 - repeating_number) % repeating_length
print(f"My number {repeating_length}")
print(f"My number {repeating_number}")
print(f"My number {number}")
new_map = data
for _ in range(0, number):
    new_map = cycle(new_map)
    print(points(new_map))

print()
print("Done")
print(points(new_map))

