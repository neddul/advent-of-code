with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

blocks = []
for x in rows:
    x, y = x.split(',')
    blocks.append((int(x), int(y)))


# Directions (North, South, West, East)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# A* algorithm implementation
def a_star(grid, start, goal):
    # Heuristic: Manhattan distance
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Check if a position is valid (within bounds and not blocked)
    def is_valid(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[y][x] != '#'

    # Initialize the open and closed sets
    open_set = [start]  # List of nodes to explore
    closed_set = set()  # Set of nodes we've already explored
    
    # Dictionary to store the cost of each node
    g_score = {start: 0}  # g(n) = cost to get to this node from start
    f_score = {start: heuristic(start, goal)}  # f(n) = g(n) + h(n)

    # Dictionary to store the best path
    came_from = {}  # A map of node to its parent, for path reconstruction

    while open_set:
        # Find the node in the open set with the lowest f_score
        current = min(open_set, key=lambda node: f_score.get(node, float('inf'))) # if node in scores, return that, else inf
        
        # If we reach the goal, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()  # Reverse the path to start from the beginning
            return path[1:]

        # Move the current node from open to closed set
        open_set.remove(current)
        closed_set.add(current)

        # Explore neighbors (North, South, West, East)
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)
            
            # Skip invalid neighbors (out of bounds or blocked)
            if not is_valid(neighbor[0], neighbor[1]) or neighbor in closed_set:
                continue
            
            # Calculate tentative g_score for the neighbor
            tentative_g_score = g_score[current] + 1  # 1 is the cost to move to the neighbor
            
            # If the neighbor is not in open_set or we found a better path to it
            if neighbor not in open_set or tentative_g_score < g_score.get(neighbor, float('inf')):
                # Set the best path to this neighbor
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)

                # Add neighbor to open set if it's not there already
                if neighbor not in open_set:
                    open_set.append(neighbor)

    return None  # Return None if there is no path

grid_size = 70
start = (0,0)
goal = (grid_size, grid_size)

my_bytes = 12
MAP = [['.']*(grid_size+1) for _ in range((grid_size+1))]
for i in range(my_bytes):
        x, y = blocks[i]
        MAP[y][x] = '#'

p1 = a_star(MAP, start, goal)
print(len(p1))


# for j in range(len(blocks)):
#     print(j)
#     MAP = [['.']*(grid_size+1) for _ in range((grid_size+1))]
#     last_block = len(blocks) - j
#     for i in range(last_block):
#         x, y = blocks[i]
#         MAP[y][x] = '#'
#     p1 = a_star2(MAP, start, goal)
#     if p1:
#         break
#     MAP = []

# print(last_block, blocks[last_block])
# print(3039, blocks[3039])
# not 38,69 - 3039
# not 58,14 - 3040
# not 56,68 - 3041
# 43,12 - 2990