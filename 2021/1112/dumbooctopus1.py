with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
rows = [[int(x) for x in row] for row in rows]

def print_rows(rows):
    print()
    for row in rows:
        string = ""
        for r in row:
            string += str(r)
        print(string)
    print()

def step(indices, arr):
    for x, y in indices:
        arr[x][y] +=1
    return arr

def increase_energy(arr):
    #Increase energy level by 1 for all octopi
    for y in range(len(arr)):
        row = arr[y]
        for x in range(len(row)):
            arr[y][x] +=1

def get_neighbors(x,y, arr, diagonals=False):
    neighbors = []
    len_cols = len(arr[0]) - 1
    len_rows = len(arr) - 1
    if diagonals:
        for dy in range(-1,2):
            for dx in range(-1,2):
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

def count_flashes(arr):
    #Check for flashes
    flashes = 0
    visited = set([])
    new_flashes = 1
    while new_flashes > 0:
        new_flashes = 0
        for y in range(len(arr)):
            row = arr[y]
            for x in range(len(row)):
                if arr[y][x] > 9 and (y,x) not in visited:
                    neighbors = get_neighbors(y, x, arr, diagonals=True)
                    step(neighbors, arr)

                    visited.add((y,x))
                    new_flashes+=1
        flashes += new_flashes
    return flashes

def reset_flashed(arr):
    #Sets newly flashed octopi to energy level 0
    for y in range(len(arr)):
            row = arr[y]
            for x in range(len(row)):
                if arr[y][x] > 9:
                    arr[y][x] = 0

flashes = 0
for _ in range(100):
    increase_energy(rows)
    energy_flash = count_flashes(rows)

    flashes += energy_flash
    reset_flashed(rows)        

print(flashes)






