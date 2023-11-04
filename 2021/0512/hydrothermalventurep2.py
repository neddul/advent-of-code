# #Part one
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [row.replace(" -> ", " ").replace(",", " ").split() for row in rows]
rows = [[int(x) for x in data] for data in rows]
one_d_list = [element for sublist in rows for element in sublist]
maxvalue = max(one_d_list)

diagram = []
for _ in range(maxvalue+1):
    points = [0]*(maxvalue+1)
    diagram.append(points)


for line in rows:
    #Horizontal and vertical lines
    x1, x2, y1, y2 = line[0], line[2], line[1], line[3]
    if x1 == x2:
        if y1 > y2:
            for i in range(y2, y1+1):
                diagram[i][x1] +=1
        else:
            for i in range(y1, y2+1):
                diagram[i][x1] +=1
    elif y1 == y2:
        if x1 > x2:
            for i in range(x2, x1+1):
                diagram[y1][i] +=1
        else:
            for i in range(x1, x2+1):
                diagram[y1][i] +=1
    if x1 < x2:
        if y1 < y2: # 1,1 -> 3,3
            while x1 <= x2:
                diagram[y1][x1] += 1
                x1 +=1
                y1 +=1
        if y1 > y2:      # 1, 3 -> 3,1
            while x1 <= x2:
                diagram[y1][x1] += 1
                x1 +=1
                y1 -=1
    elif x1 > x2:
        if y1 < y2: # 3, 1 -> 1, 3
            while x1 >= x2:
                diagram[y1][x1] += 1
                x1 -=1
                y1 +=1
        elif y1 > y2:       # 3,3 -> 1,1
            while x1 >= x2:
                diagram[y1][x1] += 1
                x1 -=1
                y1 -=1





def print_board(diagram):
    for row in diagram:
        print(row)
print_board(diagram)
two_counter = 0
for row in diagram:
    for point in row:
        if point > 1:
            two_counter +=1

print(two_counter)



