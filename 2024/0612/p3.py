with open("input_test.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
print(rows)

rows = [list(x) for x in data.split('\n')]
print(rows)

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

def check_loop(x, y, my_map, direction):
    mapwithblock = my_map.copy()
    # print(mapwithblock[y][x-1])
    if direction == "North": mapwithblock[y][x-1] = '#'
    elif direction == "East": mapwithblock[y-1][x] = '#'
    elif direction == "South": mapwithblock[y][x+1] = '#'
    elif direction == "West": mapwithblock[y+1][x] = '#'

    my_start_pos = (x,y)
    can_take_another_step = True
    distinct_pos = set()
    local_loop_len = -1
    while(can_take_another_step):
        if direction == "North":
            if valid_pos(x, y-1):
                if mapwithblock[y-1][x] != '#': #Can go there
                    y-=1
                    distinct_pos.add((x,y))
                else: #There is a block
                    direction = "East"
            else:
                can_take_another_step = False
        elif direction == "East":
            if valid_pos(x+1, y):
                if mapwithblock[y][x+1] != '#':
                    x+=1
                    distinct_pos.add((x,y))
                else:
                    direction = "South"
            else:
                can_take_another_step = False
        elif direction == "South":
            if valid_pos(x, y+1):
                if mapwithblock[y+1][x] != '#':
                    y+=1
                    distinct_pos.add((x,y))
                else:
                    direction = "West"
            else:
                can_take_another_step = False
        elif direction == "West":
            if valid_pos(x-1, y):
                if mapwithblock[y][x-1] != '#':
                    x-=1
                    distinct_pos.add((x,y))
                else:
                    direction = "North"
            else:
                can_take_another_step = False    
        
        print(len(distinct_pos))
        if local_loop_len == len(distinct_pos):
            can_take_another_step = False
        else:
            local_loop_len = len(distinct_pos)
    return my_start_pos in distinct_pos


def steps_taken(my_map, start):
    can_take_another_step = True
    direction = "North"
    x, y = start[0], start[1]
    distinct_pos = set()
    distinct_pos.add((x,y, direction))
    loop_pos = set()

    while(can_take_another_step):
        print("yah")
        if direction == "North":
            if valid_pos(x, y-1):
                if my_map[y-1][x] != '#': #Can go there
                    if check_loop(x, y, my_map, "East"): loop_pos.add((x,y-1))
                    
                    y-=1
                    distinct_pos.add((x,y, direction))

                else: #There is a block
                    direction = "East"
            else:
                can_take_another_step = False
        elif direction == "East":
            if valid_pos(x+1, y):
                if my_map[y][x+1] != '#':
                    if check_loop(x, y, my_map, "South"): loop_pos.add((x+1,y))
                    x+=1
                    distinct_pos.add((x,y, direction))
                else:
                    direction = "South"
            else:
                can_take_another_step = False
        elif direction == "South":
            if valid_pos(x, y+1):
                if my_map[y+1][x] != '#':
                    if check_loop(x, y, my_map, "West"): loop_pos.add((x,y+1))
                    y+=1
                    distinct_pos.add((x,y, direction))
                else:
                    direction = "West"
            else:
                can_take_another_step = False
        elif direction == "West":
            if valid_pos(x-1, y):
                if my_map[y][x-1] != '#':
                    if check_loop(x, y, my_map, "North"): loop_pos.add((x-1,y))
                    x-=1
                    distinct_pos.add((x,y, direction))
                else:
                    direction = "North"
            else:
                can_take_another_step = False
        print(len(loop_pos))        
    # print(loop_pos)
    return len(set([(x,y) for (x,y,_) in list(distinct_pos)])), len(loop_pos)


p1, p2 = steps_taken(rows, start)
print(p1, p2)




