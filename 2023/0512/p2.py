with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

seed_info = [int(x) for x in rows[0][7:].split()]
seed_info = [seed_info[i:i+2] for i in range(0, len(seed_info), 2)]



# data = set()
# for s in seed_info:
#     s0, s1 = s[0], s[1]
#     data.update(range(s0, s0 + s1))
    


import concurrent.futures
def process_seed(s):
    s0, s1 = s[0], s[1]    
    return set(range(s0, s0 + s1))


with concurrent.futures.ThreadPoolExecutor(max_workers=14) as executor:
    data_sets = list(executor.map(process_seed, seed_info))

result_data = set().union(*data_sets)
seeds = list(result_data)
# print(result_data)

# print(data)




map_info = [[[int(y) for y in x.split()] for x in row.split('\n')[1:]] for row in rows[1:]]
# ranges = [{},{},{},{},{},{},{}]

# for info, r in zip(map_info, ranges):
#     for line in info:
#         destination_range_start = line[0]
#         source_range_start = line[1]
#         range_length = line[2]
#         r[(source_range_start, source_range_start+range_length -1)] = (destination_range_start, destination_range_start+range_length-1)
#         # r[source_range_start] = source_range_start + range_length -1
# print(ranges)

# seeds = []
# for s in seed_info:
#     start = s[0]
#     stop = s[1] - 1
#     for r in ranges:
#         for k, v in r.items():
#             if start >= k and stop <= v: #In the range and will behave the same
#                 if start not in seeds : seeds.append(start)
#                 if stop not in seeds : seeds.append(stop)




    
    

list_of_maps = [{},{},{},{},{},{},{}]

for s in seeds:
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


lowest_loc = 1000000000000000000000000000000000000000000000
for seed in seeds:
    key = seed
    for my_map in list_of_maps:
        key = my_map[key]
    if key < lowest_loc:
        lowest_loc = key

print(lowest_loc)


def print_maps():
    for s in seeds:
        info = []
        k = s
        info.append(k)
        for i in range(len(list_of_maps)):
            v = list_of_maps[i][k]
            info.append(v)
            k = v
        # info = [info[0]] + [info[1]]
        print(info)

# print_maps()