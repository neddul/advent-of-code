with open("input.txt",'r') as f:     data = f.read()
data = data.split('\n\n')
data = [row.split() for row in data]

def compare(first, second):
    for a,b in zip(first, second):
        if a != b:
            return False
    return True

def vertical_lines(matrix):
    height = len(matrix)
    length = len(matrix[0])
    cols = []
    for x in range(length):
        line = ""
        for y in range(height):
            line += str(matrix[y][x])
        cols.append(line)
    return cols

def horizontal_lines(matrix):
    length = len(matrix)
    rows = []
    for x in range(length):
        rows.append(matrix[x])
    return rows

def points(matrix):
    for i in range(len(matrix)-1):
        if matrix[i] == matrix[i+1]:
            if i+1 > len(matrix) / 2: # More stuff on the left side/above of the col/row
                #----------------------|--------
                right_side = matrix[i+1+1:]
                left_side = list(reversed(matrix[i-(len(right_side)):i]))
                if compare(left_side, right_side):
                    return i+1
            elif i+1 < len(matrix) / 2: # More stuff on the right side/below of the col/row
                #--------|----------------------
                left_side = list(reversed(matrix[:i]))
                right_side = matrix[i+1+1:i+1+1 + (len(left_side))]
                if compare(left_side, right_side):
                    return i+1
            elif i+1 == len(matrix) / 2: #Meet in the middle
                #---------------|---------------
                left_side = list(reversed(matrix[:i]))
                right_side = matrix[i+1+1:]
                if compare(left_side, right_side):
                    return i+1
    return 0

my_sum = 0
for d in data:
    rows = horizontal_lines(d)
    cols = vertical_lines(d)
    my_sum+= points(rows) * 100
    my_sum+= points(cols)
print(my_sum)