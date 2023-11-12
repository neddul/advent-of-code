with open("input.txt",'r') as f:
    data = f.read()

rows = data.split('\n')

def low_point(point, neighbors):
    for x in neighbors:
        if point >= x:
            return False
    return True

def get_neighbors(x, y, board, neighbors):
    if y-1 >= 0 and y-1 <=len(board)-1 and x >=0 and x <= len(board[0])-1 and (y-1, x) not in neighbors:
        if int(board[y-1][x]) < 9 :
            neighbors.append((y-1, x))
            get_neighbors(x, y-1, board, neighbors)
        
    if y+1 >= 0 and y+1 <=len(board)-1 and x >=0 and x <= len(board[0])-1 and (y+1, x) not in neighbors:
        if int(board[y+1][x]) < 9 :
            neighbors.append((y+1, x))
            get_neighbors(x, y+1, board, neighbors)
        
    if y >= 0 and y <=len(board)-1 and x-1 >=0 and x-1 <= len(board[0])-1 and (y, x-1) not in neighbors :
        if int(board[y][x-1]) < 9 :
            neighbors.append((y, x-1))
            get_neighbors(x-1, y, board, neighbors)
        
    if y >= 0 and y <=len(board)-1 and x+1 >=0 and x+1 <= len(board[0])-1 and (y, x+1) not in neighbors:
        if int(board[y][x+1]) < 9 :
            neighbors.append((y, x+1))
            get_neighbors(x+1, y, board, neighbors)

def basin_size(x, y, board):
    neighbors = [(y, x)]
    get_neighbors(x, y, board, neighbors)    
    return len(neighbors)

risk_sum = 0
basins = []
for y in range(len(rows)):
    row = rows[y]
    for x in range(len(row)):
        islowpoint = False
        if y == 0 and x == 0: #upper left corner
            islowpoint = low_point(row[x], [row[x+1], rows[y+1][0]])
        elif y == 0 and x > 0 and x < len(row)-1: #upper edge
            islowpoint = low_point(row[x], [row[x+1], row[x-1], rows[y+1][x]])
        elif y == 0 and x == len(row)-1: #Upper right corner
            islowpoint = low_point(row[x], [row[x-1], rows[y+1][x]])
        elif y > 0 and y < len(rows)-1 and x == 0: #Left edge
            islowpoint = low_point(row[x], [row[x+1], rows[y+1][x], rows[y-1][x]])
        elif y == len(rows)-1 and x == 0: #lower left corner
            islowpoint = low_point(row[x], [row[x+1], rows[y-1][x]])
        elif y == len(rows)-1 and x > 0 and x < len(row)-1: #lower edge
            islowpoint = low_point(row[x], [row[x+1], row[x-1], rows[y-1][x]])
        elif y == len(rows)-1 and x == len(row)-1: #lower right corner
            islowpoint = low_point(row[x], [row[x-1], rows[y-1][x]])
        elif y > 0 and y < len(rows)-1 and x == len(row)-1: #right edge
            islowpoint = low_point(row[x], [row[x-1], rows[y+1][x], rows[y-1][x]])
        else: #Any case not on the border
            islowpoint = low_point(row[x], [row[x-1], row[x+1], rows[y+1][x], rows[y-1][x]])
        
        if islowpoint:
            risk_sum+=int(row[x])+1
            basins.append(basin_size(x, y, rows))

print(risk_sum)
basin = 1
for x in list(reversed(sorted(basins)))[:3]:
    basin*=x
print(basin)    