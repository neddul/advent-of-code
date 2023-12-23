with open("input_test.txt",'r') as f:     data = f.read().split()

def get_neighbors(matrix, y, x):
    neighbors, len_cols, len_rows = [], len(matrix[0]) - 1, len(matrix) - 1

    if y + 1 <= len_cols: neighbors.append((y+1, x))
    if y - 1 >= 0: neighbors.append((y-1, x))
    if x + 1 <= len_rows: neighbors.append((y, x+1))
    if x - 1 >= 0: neighbors.append((y, x-1))
    return neighbors

def get_column(lst, index): return [string[index] for string in lst]


def mirror(matrix, error_con):
    for i in range(0, len(matrix)-1):
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

a = list(range(10))
print(a)