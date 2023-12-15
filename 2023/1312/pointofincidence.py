with open("input.txt",'r') as f:     data = f.read()
data = data.split('\n\n')
data = [row.split() for row in data]

def rotate(matrix):
    new_map = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[-1-j][i])
        new_map.append(new_row)
    return new_map

def mirror(matrix, error_con):
    for i in range(1, len(matrix)):
        above = matrix[:i][::-1] #Reverses the strings instead of [1, 2, 3] you get [3, 2, 1]
        below = matrix[i:]
        errors = 0
        for above_row, below_row in zip(above, below): #Will be as long as the shortest list of strings
            for ac, bc in zip(above_row, below_row):
                if ac != bc:
                    errors += 1
        if errors == error_con: 
            return i
    return 0

def mirror_points(data, error_con):
    total_points = 0
    for d in data:
        row_points = mirror(d, error_con) * 100
        total_points += row_points
        d = rotate(d)
        col_points = mirror(d, error_con)
        total_points+= col_points
    return total_points

print(f"P1: {mirror_points(data, error_con=0)}")
print(f"P2: {mirror_points(data, error_con=1)}")