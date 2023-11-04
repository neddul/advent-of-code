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

lines = []
for line in rows:
    if line[0] == line[2] or line[1] == line[3]:
        lines.append(line)


for line in lines:
    if line[0] == line[2]:
        if line[1] > line[3]:
            for i in range(line[3], line[1]+1):
                diagram[line[0]][i] +=1
        else:
            for i in range(line[1], line[3]+1):
                diagram[line[0]][i] +=1
    else:
        if line[0] > line[2]:
            for i in range(line[2], line[0]+1):
                diagram[i][line[1]] +=1
        else:
            for i in range(line[0], line[2]+1):
                diagram[i][line[1]] +=1

two_counter = 0
for row in diagram:
    for point in row:
        if point > 1:
            two_counter +=1

print(two_counter)



