with open("test.txt",'r') as f:
    data = f.read()
rows = data.split(',')
import math

p1 = 0
p2 = 0

my_set = set()

def test_num(number):
    test = False
    for size in range(1, math.ceil(len(number)/2) + 2):
        if test:
            return int(number)

        start = number[:size]
        succ = True
        for i in range(size, len(number), size):
            chunk = number[i:i+size]
            print(start, chunk, succ)
            if chunk != start:
                succ = False
                break
        
        if succ:
            test = True
    return 0

for row in rows:
    start, stop = row.split('-')
    for i in range(int(start), int(stop)+1):
        if len(str(i)) > 1:
            start_half = str(i)[:int((len(str(i))/2))]
        else:
            start_half = str(i)

        t_id = int(start_half*2)
        if t_id >= int(start) and t_id <= int(stop):
            my_set.add(t_id)

        p2 += test_num(str(i))
        
print(p2)
