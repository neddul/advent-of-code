with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [list(x) for x in rows]
x_axis = len(rows[0])
y_axis = len(rows)

def valid_pos(x, y):
    valid = True
    if not (x >= 0 and x < x_axis):
        valid = False
    if not (y >= 0 and y < y_axis):
        valid = False
    return valid

def get_neighbors(sy, sx):
    potential_neighbors = [(sy-1, sx-1), (sy-1, sx), (sy-1, sx+1), (sy, sx-1), (sy, sx+1), (sy+1, sx-1), (sy+1, sx), (sy+1, sx+1)]
    valid_neighbors = []
    for y, x in potential_neighbors:
        if valid_pos(x, y):
            valid_neighbors.append((y, x))
    return valid_neighbors

def check_valid(positions, data):
    counter = 0
    for y, x in positions:
        if data[y][x] == '@':
            counter +=1
    return counter < 4


p1 = 0
for y in range(y_axis):
    for x in range(x_axis):
        if rows[y][x] == '@':
            if check_valid(get_neighbors(y,x), rows):
                p1 += 1

changed = True
p2 = 0
while changed:
    changed = False
    for y in range(y_axis):
        for x in range(x_axis):
            if rows[y][x] == '@':
                if check_valid(get_neighbors(y,x), rows):
                    p2 += 1
                    rows[y][x] = '.'
                    changed = True
    
print(p1)
print(p2)

            