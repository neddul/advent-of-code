with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
rows = [list(x) for x in rows]

def expand_universe(universe, extra_space=1):
    #Rows
    indices = []
    for i in range(len(universe)):
        row = universe[i]
        should_expand = True
        for point in row:
            if point == '#': #There is a galaxy in the row
                should_expand = False
        if should_expand:
            indices.append(i)
    for i in range(len(indices)):
        new_rows = [extra_space]*len(universe[i+indices[i]])
        universe = universe[:indices[i]+i] + [new_rows] + universe[indices[i]+i:]
    #Columns
    indices = []
    for i in range(len(universe[0])):
        should_expand = True
        for j in range(len(universe)):
            if universe[j][i] == '#': #There is a galaxy in the column
                should_expand = False
        if should_expand:
            indices.append(i)
    for i in range(len(indices)):
        for j in range(len(universe)):
            universe[j] = universe[j][:indices[i]+i] + [extra_space] + universe[j][indices[i]+i:]
    return universe

def galaxy_locations(universe, space_size=1):
    galaxies = []
    offsety = 0
    for i in range(len(universe)):
        offsetx = 0
        m = len(universe[i])
        for j in range(m):
            if universe[i][j] not in {'.', '#'}:
                offsetx+=1
            if universe[i][j] == '#': #A galaxy
                space_size_offset = space_size - 1 if space_size > 1 else space_size
                galaxies.append((i+offsety*(space_size_offset-1), j+offsetx*(space_size_offset-1)))
            if offsetx == m:
                offsety+=1
    return galaxies
       
def distance_to_other_galaxies(my_galaxy_locations):
    cumsum = 0
    for i in range(len(my_galaxy_locations)):
        g = my_galaxy_locations[i]
        for other_locations in my_galaxy_locations[i:]:
            distance = abs(g[0] - other_locations[0]) + abs(g[1] - other_locations[1])
            cumsum+=distance
    return cumsum
part1 = 1
part2 = 1_000_000
print(f"Part 1: {distance_to_other_galaxies(galaxy_locations(expand_universe(rows, part1), part1))}")
print(f"Part 2: {distance_to_other_galaxies(galaxy_locations(expand_universe(rows, part2), part2))}")