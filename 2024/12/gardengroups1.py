with open("input.txt",'r') as f:
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

def mark_region(x, y, area):
    def region(neighbors, start_value):
        for x, y in neighbors:
            if valid_pos(x, y):
                if area[y][x] == start_value and (x,y) not in region_positions:
                    region_positions.add((x, y))
                    new_neighbors = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
                    region(new_neighbors, start_value)
            
    region_positions = set()
    start_value = area[y][x]
    region_positions.add((x, y))
    neighbors = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
    region(neighbors, start_value)
    return region_positions

def mark_fences(region_pos, area):
    fence_pos = set()
    sx, sy = list(region_pos)[0]
    start_value = area[sy][sx]
    for x, y in region_pos:
        neighbors = [(x-1,y), (x+1,y), (x, y-1), (x, y+1)]
        for nx, ny in neighbors:
            if not valid_pos(nx, ny) or area[ny][nx] != start_value:
                fence_pos.add(((nx, ny), (nx-x, ny-y)))
    return fence_pos

used_regions = set()
areas_and_fences = dict()

for y in range(y_axis):
    for x in range(x_axis):
        if (x, y) not in used_regions:
            region = mark_region(x, y, rows)
            fences = mark_fences(region, rows)
            print(fences)
            

            areas_and_fences[(x,y)] = (len(region), len(fences))
            used_regions.update(region)

p1 = 0
p2 = 0
for area, fence,  in areas_and_fences.values():
    p1 += area*fence

print(p1)

