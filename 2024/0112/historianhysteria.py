with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

leftside = []
rightside = []
for row in rows:
    a = row.split()
    leftside.append(int(a[0]))
    rightside.append(int(a[1]))

leftside.sort()
rightside.sort()

my_sum = 0
my_sum2 = 0
for l, r in zip(leftside, rightside):
    my_sum += abs(l-r)
    my_sum2 += l * rightside.count(l) #part 2

print(my_sum)
print(my_sum2)