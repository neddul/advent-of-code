with open("input.txt",'r') as f:
    data = f.read()
rows = [list(x) for x in data.split('\n')]
x_axis = len(rows[0])
y_axis = len(rows)

print(rows)
def valid_pos(x, y):
    valid = True
    if not (x >= 0 and x < x_axis):
        valid = False
    if not (y >= 0 and y < y_axis):
        valid = False
    return valid

def create_antinode(freq, startx, starty):
    freq_set = set()
    for y in range(y_axis):
        for x in range(x_axis):
            new_freq = rows[y][x]
            if new_freq == freq and x != startx and y != starty:
                
                dx = 2 * (x - startx)
                dy = 2 * (y - starty)

                if valid_pos(dx+startx, dy+starty):
                    freq_set.add((dx+startx, dy+starty))
    return freq_set

antinodes = set()
for y in range(y_axis):
    for x in range(x_axis):
        freq = rows[y][x]
        if freq != '.':
            antinodes.update(create_antinode(freq, x, y))
print(len(antinodes))