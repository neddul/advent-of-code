with open("input.txt",'r') as f:
    data = f.read()
rows = [list(x) for x in data.split('\n')]
x_axis = len(rows[0])
y_axis = len(rows)

def valid_pos(x, y):
    valid = True
    if not (x >= 0 and x < x_axis):
        valid = False
    if not (y >= 0 and y < y_axis):
        valid = False
    return valid

def check_if_antinode(freq, startx, starty, freq_set, dx, dy):
    i = 1
    while (valid_pos(startx+dx*i, starty+dy*i)):
        if rows[starty+dy*i][startx+dx*i] == freq or (startx+dx*i, starty+dy*i) in freq_set:
            return True
        i+=1
    return False
    
def create_antinode(freq, startx, starty):
    freq_set = set()
    for y in range(y_axis):
        for x in range(x_axis):
            new_freq = rows[y][x]
            if new_freq == freq and x != startx and y != starty:
                multiplier = 2
                while (True):
                    dx = multiplier * (x - startx)
                    dy = multiplier * (y - starty)

                    if valid_pos(dx+startx, dy+starty):
                        freq_set.add((dx+startx, dy+starty))
                        multiplier +=1
                    else:
                        break
    return freq_set

antinodes = set()

for y in range(y_axis):
    for x in range(x_axis):
        freq = rows[y][x]
        if freq != '.':
            antinodes.update(create_antinode(freq, x, y))

for y in range(y_axis):
    for x in range(x_axis):
        freq = rows[y][x]
        if freq != '.':
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] # N S W E
            for dx, dy in directions:
                if check_if_antinode(freq, x, y, antinodes, dx, dy):
                    antinodes.add((x, y))
            
print(len(antinodes))
