with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
from collections import defaultdict
my_dict = defaultdict(list)

for row in rows:
    key, values = row.split(': ')
    for value in values.split(" "):
        my_dict[key].append(value)

def paths(ye):
    cache = {}
    def aux(key):
        if key == "you":
            return 0 # to avoid loops
        if key in cache:
            return cache[key]
        if my_dict[key][0] == "out":
            return 1
        if key not in my_dict:
            return 0
        
        cache[key] = sum([aux(k) for k in my_dict[key]])
        return cache[key]
    return aux(ye)

p1 = 0
for v in my_dict["you"]:
    p1 += paths(v)

print(p1)
