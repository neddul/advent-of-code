with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def get_neighbors(x,y, arr, diagonals=False):
    neighbors = []
    len_cols = len(arr[0]) - 1
    len_rows = len(arr) - 1
    if diagonals:
        for dx in range(-1,2):
            for dy in range(-1,2):
                if x+dx < 0 or x+dx > len_cols or y+dy < 0 or y+dy > len_rows or (dx == 0 and dy == 0):
                    continue
                else:
                    neighbors.append((x+dx, y+dy))
    else:
        if x + 1 < len_cols:
            neighbors.append((x+1, y))
        if x - 1 >= 0:
            neighbors.append((x-1, y))
        if y + 1 < len_rows:
            neighbors.append((x, y+1))
        if y - 1 >= 0:
            neighbors.append((x, y-1))

    return neighbors

gears = {}
for y in range(len(rows)):    
    number = ""
    row = rows[y]
    use_number = False
    gear_loc = 0
    for x in range(len(row)):
        if row[x].isdigit():
            number+=row[x]
            if not use_number:
                neighbors = get_neighbors(y, x, rows, diagonals=True)
                for n, m in neighbors:                    
                    if rows[n][m] == '*':
                        gear_loc = (n,m)
                        use_number = True
                        if (n,m) in gears:
                            continue
                        else:
                            gears[(n,m)] = []
        else:
            if not use_number:
                number = ""
                continue
            else:
                use_number = False
                gears[gear_loc].append(int(number))
                number = ""
    if len(number) > 0 and use_number:        
        use_number = False
        gears[gear_loc].append(int(number))
        number = ""

summ = 0
for k,v in gears.items():
    if len(v) == 2:
        summ+= v[0] * v[1]
    
print(summ)