with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
startpos = ([i for i, ch in enumerate(rows[0]) if ch in "S"][0], 0) # start x,y

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

p1 = 0
paths = dict()

for y in range(y_axis):
    new_beams = []
    for x in range(x_axis):
        
        if rows[y][x] == 'S' or rows[y][x] == '|':
            new_beams.append((x, y+1))
    
    for bx, by in new_beams:
        if valid_pos(bx, by):
            #Create new beam
            if rows[by][bx] == '.' or rows[by][bx] == '|':                
                rows[by][bx] = '|'

                if rows[by-1][bx] == '|':
                    if (bx,by) in paths:
                        paths[(bx,by)].append((bx, by-1))
                    else:
                        paths[(bx,by)] = [(bx, by-1)]

            
            elif rows[by][bx] == '^':
                p1 += 1
                splits = [(bx-1, by), (bx+1, by)]
                for bx2, by2 in splits:
                    rows[by2][bx2] = '|'
                
                    if (bx2, by2) in paths:
                        paths[(bx2, by2)].append((bx, by-1))
                    else:
                        paths[(bx2, by2)] = [(bx, by-1)]
        

bottoms = []
for k, v in paths.items():
    x, y = k
    if y == y_axis-1:
        bottoms.append(k)

def count_paths_to_start(graph, current, start, memo=None, visited=None):
    # Set up memo and visited on first call
    if memo is None:
        memo = {}
    if visited is None:
        visited = set()
    
    # If we've reached the starting coordinate, we've found 1 path
    if current == start:
        return 1
    
    # If we already computed from this node, reuse it
    if current in memo:
        return memo[current]
    
    # Cycle protection: if we're revisiting a node in the same path, stop
    if current in visited:
        return 0
    
    visited.add(current)
    
    total = 0
    # Get neighbors; if current not in graph, treat as dead end
    for nxt in graph.get(current, []):
        total += count_paths_to_start(graph, nxt, start, memo, visited)
    
    visited.remove(current)
    
    memo[current] = total
    return total


p2 = 0
for bot in bottoms:
    p2 += count_paths_to_start(paths, bot, start=(startpos[0], startpos[1]+1))
    
print(p1)
print(p2)
