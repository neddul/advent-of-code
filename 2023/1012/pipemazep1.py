with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
# print(rows)

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
        if x + 1 <= len_cols:
            neighbors.append((x+1, y))
        if x - 1 >= 0:
            neighbors.append((x-1, y))
        if y + 1 <= len_rows:
            neighbors.append((x, y+1))
        if y - 1 >= 0:
            neighbors.append((x, y-1))

    return neighbors

def find_start(arr):
    for y in range(len(arr)):
        row = arr[y]
        for x in range(len(row)):
            if arr[y][x] == 'S':
                return (y, x)
    print("No start found")
    return (-1, -1)

def vertical_pipe(pipe_point):
    return [(pipe_point[0]-1, pipe_point[1]), (pipe_point[0]+1, pipe_point[1])]
    
def horizontal_pipe(pipe_point):
    return [(pipe_point[0], pipe_point[1]-1), (pipe_point[0], pipe_point[1]+1)]

def L_pipe(pipe_point):
    return [(pipe_point[0]-1, pipe_point[1]), (pipe_point[0], pipe_point[1]+1)]

def J_pipe(pipe_point):
    return [(pipe_point[0], pipe_point[1]-1), (pipe_point[0]-1, pipe_point[1])]

def Seven_pipe(pipe_point):
    return [(pipe_point[0], pipe_point[1]-1), (pipe_point[0]+1, pipe_point[1])]
    
def F_pipe(pipe_point):
    return [(pipe_point[0], pipe_point[1]+1), (pipe_point[0]+1, pipe_point[1])]

def S_pipe(pipe_point):
    return [(pipe_point[0], pipe_point[1]+1), (pipe_point[0], pipe_point[1]-1), (pipe_point[0]+1, pipe_point[1]), (pipe_point[0]-1, pipe_point[1])]


def move_through_loop(neighbor, arr):
    pipe_shape = arr[neighbor[0]][neighbor[1]]
    if   pipe_shape == '|': return vertical_pipe(neighbor)
    elif pipe_shape == '-': return horizontal_pipe(neighbor)
    elif pipe_shape == 'L': return L_pipe(neighbor)
    elif pipe_shape == 'J': return J_pipe(neighbor)
    elif pipe_shape == '7': return Seven_pipe(neighbor)
    elif pipe_shape == 'F': return F_pipe(neighbor)
    elif pipe_shape == 'S': return S_pipe(neighbor)
    else: return [] # print("No valid pipes found")
            

def find_loop_length(arr, visited_positions):
    my_moves = [1,2,3,4] #Random stuff to start while loop
    start_pos = find_start(arr)
    i = 1
    while len(my_moves) > 0:
        my_moves = move_through_loop(start_pos, arr)
        my_moves = [possible_move for possible_move in my_moves if possible_move not in visited_positions]
        neighbors = get_neighbors(start_pos[0], start_pos[1], arr)
        for neighbor in neighbors:
            possible_moves = move_through_loop(neighbor, arr)
            if start_pos in possible_moves and neighbor in my_moves:
                visited_positions.add(start_pos)
                start_pos = neighbor
                break
        i+=1
    print(i//2)

visited_positions = set()
find_loop_length(rows, visited_positions)
# print(visited_positions)

