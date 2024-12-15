with open("input_test.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

moves = rows[1].replace('\n', '')
rows = [list(x) for x in rows[0].split('\n')]
    


x_axis = len(rows[0])
y_axis = len(rows)

for y in range(y_axis):
    for x in range(x_axis):
        if rows[y][x] == '#':
            rows[y][x] = '##'
        elif rows[y][x] == 'O':
            rows[y][x] = '[]'
        elif rows[y][x] == '.':
            rows[y][x] = '..'
        else:
            rows[y][x] = '@.'

rows2 = []

for ijjjj in rows:
    a = ""
    for jkkk in ijjjj:
        a += jkkk
    rows2.append(a)

rows = [list(x) for x in rows2]

x_axis = len(rows[0])
y_axis = len(rows)

for ijjjj in rows:
    a = ""
    for jkkk in ijjjj:
        a += jkkk
    print(a)

def valid_pos(x, y):
    valid = True
    if not (x >= 0 and x < x_axis):
        valid = False
    if not (y >= 0 and y < y_axis):
        valid = False
    return valid

angler_pos = (-1, -1)
for y in range(y_axis):
    for x in range(x_axis):
        if rows[y][x] == '@':
            angler_pos = (x, y)
    if angler_pos != (-1,-1):
        break

def affect_boxes(MAP, x, y, dy):
    if MAP[y + 1*dy][x] == '[' or MAP[y + 1*dy][x] == ']':
        




def move_anglerfish(MAP, dx, dy, angler_pos):
    sx, sy = angler_pos[0], angler_pos[1]
    nx, ny = sx + 1*dx, sy + 1*dy

    if valid_pos(nx, ny):        
        if MAP[ny][nx] == '.':
            MAP[ny][nx] = '@'
            MAP[sy][sx] = '.'
            angler_pos = (nx, ny)
        
        elif MAP[ny][nx] == '#':
            angler_pos = (sx, sy)
        
        else:
            if dy == 1:
                if MAP[ny][nx] == '[':


            elif dy == -1:

            nnx, nny = nx + 1*dx, ny + 1*dy
            succ = False
            while valid_pos(nnx, nny):
                if MAP[nny][nnx] == 'O':
                    nnx += 1*dx
                    nny += 1*dy
                elif MAP[nny][nnx] == '.':
                    succ = True
                    break
                else:
                    break
            
            if succ:
                MAP[nny][nnx] = 'O'
                MAP[ny][nx] = '@'
                MAP[sy][sx] = '.'
                angler_pos = (nx, ny)
        
    return MAP, angler_pos

for move in moves:
    if move == '^':
        rows, angler_pos = move_anglerfish(rows, 0, -1, angler_pos)
    elif move == 'v':
        rows, angler_pos = move_anglerfish(rows, 0, 1, angler_pos)
    elif move == '<':
        rows, angler_pos = move_anglerfish(rows, -1, 0, angler_pos)
    else:        
        rows, angler_pos = move_anglerfish(rows, 1, 0, angler_pos)
    
p1 = 0

for y in range(y_axis):
    for x in range(x_axis):
        if rows[y][x] == 'O':
            p1 += 100 * y + x

print(p1)
