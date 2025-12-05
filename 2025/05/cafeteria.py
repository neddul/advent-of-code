with open("input.txt",'r') as f:
    data = f.read()
ranges, ids = data.split('\n\n')

ids = [int(x) for x in ids.split('\n')]
ranges = ranges.split('\n')

p1 = 0
for id in ids:
    is_in = False
    for id_ranges in ranges:
        start, stop = id_ranges.split('-')
        if id >= int(start) and id <= int(stop):
            is_in = True
            break

    if is_in:
        p1+=1

print(p1)

changed = True
while changed:
    changed = False
    for i in range(len(ranges)):
        my_range = ranges.pop(i)
        start, stop = my_range.split('-')
        start, stop = int(start), int(stop)
        for j in range(len(ranges)):
            
            new_my_range = ranges.pop(j)
            new_start, new_stop = new_my_range.split('-')
            new_start, new_stop = int(new_start), int(new_stop)

            if start >= new_start and start <= new_stop:
                last_num = new_stop if new_stop > stop else stop
                ranges.append(f"{new_start}-{last_num}")
                changed = True
                break
            elif stop >= new_start and stop <=new_stop:
                first_num = start if start < new_start else new_start
                ranges.append(f"{first_num}-{new_stop}")
                changed = True
                break
            else:
                ranges.insert(j, new_my_range)

        if changed:
            break
        ranges.insert(i, my_range)

p2 = 0

for range in ranges:
    start, stop = range.split('-')
    p2 += (int(stop) - int(start) + 1)

print(p2)
