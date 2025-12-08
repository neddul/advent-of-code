with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
import math, time


def euclidean(p, q):
    x1,y1,z1 = p.split(',')
    x2,y2,z2 = q.split(',')
    return abs( math.sqrt((int(x1)-int(x2))**2 + (int(y1)-int(y2))**2 + (int(z1)-int(z2))**2))

distances = []

for i in range(len(rows)):
    comp = rows.pop(i)
    for j in range(len(rows)):
        d = euclidean(comp, rows[j])

        distance = sorted([comp, rows[j]])
        distances.append((distance[0], distance[1], d))
        
    rows.insert(i, comp)

distances = sorted(list(set((distances))), key=lambda x: x[2])


def func(distances, p1):
    junctions = []
    additions = 0
    for a, b, d in distances:
        if p1:
            if additions == 1000:
                break    

        a_set = set()
        b_set = set()
        for junction in junctions:
            if a in junction:
                a_set = junction
            if b in junction:
                b_set = junction
        
        if a_set == set() and b_set == set():
            new_junction = set()
            new_junction.add(a)
            new_junction.add(b)
            junctions.append(new_junction)
            additions += 1
        elif a_set == set() and b_set != set():
            junction = junctions.pop(junctions.index(b_set))
            junction.add(a)
            junctions.append(junction)
            additions += 1
        elif a_set != set() and b_set == set():
            junction = junctions.pop(junctions.index(a_set))
            junction.add(b)
            junctions.append(junction)
            additions += 1
        elif a_set != b_set:
            a_junction = junctions.pop(junctions.index(a_set))
            b_junction = junctions.pop(junctions.index(b_set))
            merged_junction = a_junction.union(b_junction)
            junctions.append(merged_junction)
            additions += 1
        elif a_set == b_set:
            additions += 1
        
        if len(junctions) == 1:
            if len(junctions[0]) == len(rows):
                x1,_,_ = a.split(',')
                x2,_,_ = b.split(',')
                print(int(x1) * int(x2))
                return
    lens = list(reversed(sorted([len(x) for x in junctions])))
    print(lens[0] * lens[1] * lens[2])
    return

func(distances, True)
func(distances, False)
