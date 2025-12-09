with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def find_area(point):
    x1, y1 = point[0].split(',')
    x2, y2 = point[1].split(',')
    l1 = abs(int(x1)-int(x2))+1
    l2 = abs(int(y1)-int(y2))+1
    return l1*l2

rects = []

for i in range(len(rows)):
    comp = rows.pop(i)
    for j in range(len(rows)):
        d = find_area((comp, rows[j]))

        distance = sorted([comp, rows[j]])
        rects.append((distance[0], distance[1], d))
        
    rows.insert(i, comp)

rects = list(reversed(sorted(list(set((rects))), key=lambda x: x[2])))

print(rects[0][2])
