with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
my_dict = dict()

for row in rows:
    key, values = row.split(': ')
    my_dict[key] = values.split()

def part1(key):
    cache = {}
    def aux(key):
        if key in cache:
            return cache[key]
        if key == "out":
            return 1
        values = my_dict.get(key)
        if values is None:
            return 0
        
        cache[key] = sum([aux(k) for k in values])
        return cache[key]
    
    return sum(aux(k) for k in my_dict[key])

print(part1('you'))
