with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
rows = [list(x) for x in rows]

def expand_universe(universe, extra_space=1):
    #Rows
    indices_to_expand = []
    for i in range(len(universe)):
        row = universe[i]
        should_expand = True
        for point in row:
            if point == '#': #There is a galaxy in the row
                should_expand = False
        if should_expand:
            indices_to_expand.append(i)
    for i in range(len(indices_to_expand)):
        new_rows = [extra_space]*len(universe[i+indices_to_expand[i]])
        universe = universe[:indices_to_expand[i]+i] + [new_rows] + universe[indices_to_expand[i]+i:]
    #Columns
    indices_to_expand = []
    for i in range(len(universe[0])):
        should_expand = True
        for j in range(len(universe)):
            if universe[j][i] == '#': #There is a galaxy in the column
                should_expand = False
        if should_expand:
            indices_to_expand.append(i)
    for i in range(len(indices_to_expand)):
        for j in range(len(universe)):
            universe[j] = universe[j][:indices_to_expand[i]+i] + [extra_space] + universe[j][indices_to_expand[i]+i:]
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
                galaxies.append((i+offsety*(space_size_offset), j+offsetx*(space_size_offset)))
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
print(f"Part 1: {distance_to_other_galaxies(galaxy_locations(expand_universe(rows, 1), 1-1))}")
print(f"Part 2: {distance_to_other_galaxies(galaxy_locations(expand_universe(rows, 1_000_000), 1_000_000-1))}")