with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

print(rows)

leftside = []
rightside = []
for row in rows:
    a = row.split()
    leftside.append(int(a[0]))
    rightside.append(int(a[1]))

leftside.sort()
rightside.sort()

my_sum = 0
for l, r in zip(leftside, rightside):
    my_sum += abs(l-r)

print(my_sum)