with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

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

def start_pos(my_map):
    for y in range(len(my_map)):
        for x in range(len(my_map[0])):
            if my_map[y][x] == '^': #Always starts with ^
                return (x,y)
    return (None, None)

start = start_pos(rows)


def steps_taken(my_map, start):
    can_take_another_step, stuck_in_loop = True, False
    x, y = start[0], start[1]
    distinct_pos = set()
    distinct_pos.add((x,y))
    turns = set()
    curr_dirr = 0 # N
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)] #N E S W
    while(can_take_another_step and not stuck_in_loop):
        dx, dy = dirs[curr_dirr]
        if valid_pos(x+1*dx, y+1*dy):
            if my_map[y+1*dy][x+1*dx] == '#': #Can't go there
                if (x, y, dx, dy) not in turns:
                    turns.add((x, y, dx, dy))
                    curr_dirr = (curr_dirr + 1) % 4
                else:
                    stuck_in_loop = True #Stuck in a loop      

            else:
                x += 1*dx
                y += 1*dy
                distinct_pos.add((x,y))
        else:
            can_take_another_step = False

    if stuck_in_loop:
        distinct_pos = set()

    return distinct_pos


def check_if_loop(positions, my_map, start):
    loopcounter = 0
    i = 0
    for x, y in positions:
        my_map[y][x] = '#'
        res = steps_taken(my_map, start)
        my_map[y][x] = '.'
        if len(res) == 0:
            loopcounter +=1
        if (i+1) % 100 == 0:
            print("Test:", i+1)
        i+=1
    return loopcounter

p1 = steps_taken(rows, start)
print(len(p1))
print(check_if_loop(p1, rows, start))
