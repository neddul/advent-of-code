with open("input.txt",'r') as f:     data = f.read()
data = data.split('\n')
data = [list(d) for d in data]
# print(data)


def move_north(matrix, y, x):
    for i in range(y):
        if (y-1) - i >= 0:
            if matrix[(y-1) - i][x] != '.':
                break
            else:
                matrix[(y-1) - i][x] = 'O'
                matrix[(y) - i][x] = '.'
            # if matrix[(y-1) - i][x] == '.':
    return matrix

def move(matrix):
    new_board = matrix
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):        
            point = matrix[y][x]
            if point == 'O':
                new_board = move_north(new_board, y, x)
    return new_board

def print_map(data):
    for d in data:
        print(d)
north_map = move(data)

def points(matrix):
    my_sum = 0
    length = len(matrix)
    for i in range(length):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 'O':
                my_sum+=length-i
    return my_sum

my_points = points(north_map)
print(my_points)

