with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [list(x) for x in data.split('\n')]
# print(rows)

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
    can_take_another_step = True
    direction = "North"
    x, y = start[0], start[1]
    distinct_pos = set()
    distinct_pos.add((x,y))
    loop_len = -5
    i = 0
    while(can_take_another_step):
        if direction == "North":
            if valid_pos(x, y-1):
                if my_map[y-1][x] != '#': #Can go there
                    y-=1
                    distinct_pos.add((x,y))
                else: #There is a block
                    direction = "East"
            else:
                can_take_another_step = False
        elif direction == "East":
            if valid_pos(x+1, y):
                if my_map[y][x+1] != '#':
                    x+=1
                    distinct_pos.add((x,y))
                else:
                    direction = "South"
            else:
                can_take_another_step = False
        elif direction == "South":
            if valid_pos(x, y+1):
                if my_map[y+1][x] != '#':
                    y+=1
                    distinct_pos.add((x,y))
                else:
                    direction = "West"
            else:
                can_take_another_step = False
        elif direction == "West":
            if valid_pos(x-1, y):
                if my_map[y][x-1] != '#':
                    x-=1
                    distinct_pos.add((x,y))
                else:
                    direction = "North"
            else:
                can_take_another_step = False
        if loop_len == len(distinct_pos) and can_take_another_step:
            if i > 1000:
                return set()
            else:
                i += 1
        else:
            loop_len = len(distinct_pos)
    return distinct_pos


def check_if_loop(positions, my_map, start):
    loopcounter = 0
    for x,y in list(positions):
        new_map = [a.copy() for a in my_map]
        new_map[y][x] = '#'
        res = steps_taken(new_map, start)
        if len(res) == 0:
            loopcounter +=1
    return loopcounter

p1 = steps_taken(rows, start)
print(len(p1))
print(check_if_loop(p1, rows, start))

        

