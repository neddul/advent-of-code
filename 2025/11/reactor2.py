with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
my_dict = dict()

for row in rows:
    key, values = row.split(': ')
    my_dict[key] = values.split()

def part2(start):
    cache = {}
    def aux(key, fft, dac):
        state = (key, fft, dac)
        if state in cache:
            return cache[state]
        if key == "out": 
            return 1 if fft and dac else 0
        values = my_dict.get(key)
        if values is None:
            return 0

        if key == "fft":
            fft = True
        elif key == "dac":
            dac = True

        cache[state] = sum(aux(k, fft, dac) for k in values)
        return cache[state]

    return aux(start, False, False)

print(part2('svr'))
