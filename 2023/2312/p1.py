with open("input_test.txt",'r') as f:     data = f.read().split()

def get_neighbors(y, x, arr):
    neighbors = []
    len_cols = len(arr) - 1
    len_rows = len(arr[0]) - 1
    if y + 1 <= len_cols: neighbors.append((y+1, x))
    if y - 1 >= 0       : neighbors.append((y-1, x))
    if x + 1 <= len_rows: neighbors.append((y, x+1))
    if x - 1 >= 0       : neighbors.append((y, x-1))
    return neighbors

def find_start(arr): #Assuming start is always on the first row
    for x in range(len(arr[0])):
        if arr[0][x] == '.':
            return (0, x)

def possible_moves(y, x, arr, visited_positions):
    my_neighbors = get_neighbors(y, x, arr)
    #Remove forest and visited positions
    my_neighbors = [neighbor for neighbor in my_neighbors if (arr[neighbor[0]][neighbor[1]]) != '#' and neighbor not in visited_positions]
    #Remove pointy slopes

    #Invalid north 
    if y > 0: 
        if arr[y-1][x] == 'v' and (y-1, x) in my_neighbors:
            my_neighbors.remove((y-1, x))
    if y < len(arr)-1:
        if arr[y+1][x] == '^' and (y+1, x) in my_neighbors:
            my_neighbors.remove((y+1, x))
    if x > 0:
        if arr[y][x-1] == '>' and (y, x-1) in my_neighbors:
            my_neighbors.remove((y, x-1))
    if x < len(arr[y])-1:
        if arr[y][x+1] == '<' and (y, x+1) in my_neighbors:
            my_neighbors.remove((y, x+1))
    return my_neighbors

def hike(start_pos, arr, visited_positions, steps_taken=1):
    my_moves = possible_moves(start_pos[0], start_pos[1], arr, visited_positions)

    if len(my_moves) == 1:
        steps_taken +=1
        visited_positions.add(my_moves[0])
        steps_taken = hike(my_moves[0], arr, visited_positions, steps_taken)
        print(steps_taken)
    if len(my_moves) == 2:
        steps_taken +=1
        visited_positions.add(my_moves[0])
        steps_taken = hike(my_moves[0], arr, visited_positions, steps_taken)
        visited_positions.add(my_moves[1])
        steps_taken = hike(my_moves[1], arr, visited_positions, steps_taken)
    if len(my_moves) == 3:
        steps_taken +=1
        visited_positions.add(my_moves[0])
        steps_taken = hike(my_moves[0], arr, visited_positions, steps_taken)
        visited_positions.add(my_moves[1])
        steps_taken = hike(my_moves[1], arr, visited_positions, steps_taken)
        visited_positions.add(my_moves[2])
        steps_taken = hike(my_moves[2], arr, visited_positions, steps_taken)
    
    return steps_taken
    

def long_walk(arr):
    start_pos = find_start(arr)
    visited_positions = set()
    visited_positions.add(start_pos)
    print(hike(start_pos, arr, visited_positions))

print(data)

long_walk(data)