with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

x_axis = len(rows[0])
y_axis = len(rows)

def valid_pos(x, y):
    valid = True
    if not (x >= 0 and x < x_axis):
        valid = False
    if not (y >= 0 and y < y_axis):
        valid = False
    return valid

reachable_nines = set()
my_list = []

def count_reachable_nines(startpos, x, y, search_num):
    if search_num < 10:
        potential_neighbors = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        for nx, ny in potential_neighbors:
            if valid_pos(nx, ny):
                if rows[ny][nx].isnumeric():
                    if int(rows[ny][nx]) == search_num:
                        if int(rows[ny][nx]) == search_num and search_num == 9:
                            nine_pos = (nx, ny)
                            reachable_nines.add((startpos, nine_pos))
                            my_list.append(1)
                        else:
                            count_reachable_nines(startpos, nx, ny, search_num+1)

for y in range(y_axis):
    for x in range(x_axis):
        if rows[y][x].isnumeric():
            if int(rows[y][x]) == 0:
                startpos = (x, y)
                count_reachable_nines(startpos, x, y, 1)

print(len(reachable_nines)) #p1
print(len(my_list)) #p2
