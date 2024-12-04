with open("input_test3.txt",'r') as f:
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

def potential_ends(x,y):
    return [(x-3,y), (x-3,y+3), (x-3,y-3), (x,y-3), (x,y+3), (x+3,y-3), (x+3,y), (x+3,y+3)]
            #W          SW       NW         N         S        NE         E        SE

def xmas_word(x, y):
    xmas_words_counter = 0
    potential_end_pos = potential_ends(x,y)
    end_points = []
    for (px, py) in potential_end_pos:
        if valid_pos(px, py):
            end_points.append((px, py))
    
    for (px, py) in end_points:
        if px > x: # East options
            if py > y: # SE
                if rows[y+1][x+1] == 'M' and rows[y+2][x+2] == 'A' and rows[y+3][x+3] == 'S':
                    xmas_words_counter +=1
            if py < y: # NE
                if rows[y-1][x+1] == 'M' and rows[y-2][x+2] == 'A' and rows[y-3][x+3] == 'S':
                    xmas_words_counter +=1
            if py == y: #E
                if rows[y][x+1] == 'M' and rows[y][x+2] == 'A' and rows[y][x+3] == 'S':
                    xmas_words_counter +=1
        if px < x: # West options
            if py > y: # SW
                if rows[y+1][x-1] == 'M' and rows[y+2][x-2] == 'A' and rows[y+3][x-3] == 'S':
                    xmas_words_counter +=1
            if py < y: # NW
                if rows[y-1][x-1] == 'M' and rows[y-2][x-2] == 'A' and rows[y-3][x-3] == 'S':
                    xmas_words_counter +=1
            if py == y: #W
                if rows[y][x-1] == 'M' and rows[y][x-2] == 'A' and rows[y][x-3] == 'S':
                    xmas_words_counter +=1
        if px == x: # Vertical options
            if py > y: # S
                if rows[y+1][x] == 'M' and rows[y+2][x] == 'A' and rows[y+3][x] == 'S':
                    xmas_words_counter +=1
            if py < y: # N
                if rows[y-1][x] == 'M' and rows[y-2][x] == 'A' and rows[y-3][x] == 'S':
                    xmas_words_counter +=1
    return xmas_words_counter

def needed_neighbors(x,y):
    succ = True
    neighbors = [(x-1, y-1), (x-1, y+1), (x+1, y+1), (x+1, y-1)]
                #   NW          SW          SE          NE
    
    for (px, py) in neighbors:
        if not valid_pos(px, py):
            succ = False
            break
    return succ

def mas_cross(x,y):
    succ = False
    if needed_neighbors(x,y): 
        if ((rows[y-1][x-1] == 'M' and rows[y+1][x+1] == 'S') or (rows[y-1][x-1] == 'S' and rows[y+1][x+1] == 'M')) and ((rows[y+1][x-1] == 'M' and rows[y-1][x+1] == 'S') or (rows[y+1][x-1] == 'S' and rows[y-1][x+1] == 'M')):
            succ = True
    return succ

xmas_words = 0
x_mas = 0

for y in range(y_axis):

    for x in range(x_axis):
        if rows[y][x] == 'X':
            xmas_words += xmas_word(x,y)
        if rows[y][x] == 'A':
            if mas_cross(x,y):
                x_mas += 1

print(xmas_words)
print(x_mas)
