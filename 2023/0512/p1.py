with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

seed_info = [int(x) for x in rows[0][7:].split()]
map_info = [[[int(y) for y in x.split()] for x in row.split('\n')[1:]] for row in rows[1:]]

list_of_maps = [{},{},{},{},{},{},{}]

for s in seed_info:
    k = s
    for d, info in zip(list_of_maps, map_info):
        d[k] = k    
        for line in info:
            destination_range_start = line[0]
            source_range_start = line[1]
            range_length = line[2]
            if source_range_start <= k and source_range_start + range_length > k: # Value will be affected
                diff = abs(destination_range_start-source_range_start)
                if source_range_start >= destination_range_start:
                    d[k] -= diff
                else:            
                    d[k] += diff
        k = d[k]


def print_maps():
    for s in seed_info:
        info = []
        k = s
        info.append(k)
        for i in range(len(list_of_maps)):
            v = list_of_maps[i][k]
            info.append(v)
            k = v
        print(info)


lowest_loc = 1000000000000000000000000000000000000000000000
for seed in seed_info:
    key = seed
    for my_map in list_of_maps:
        key = my_map[key]
    if key < lowest_loc:
        lowest_loc = key

print(lowest_loc)