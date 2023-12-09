with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n\n')

seed_info = [int(x) for x in rows[0][7:].split()]
seed_info = [seed_info[i:i+2] for i in range(0, len(seed_info), 2)]

seed_ranges = []
for seeds in seed_info:
    seed_ranges.append((seeds[0], seeds[0]+seeds[1] -1))
print(seed_ranges)


map_info = [[[int(y) for y in x.split()] for x in row.split('\n')[1:]] for row in rows[1:]]
map_range = [{},{},{},{},{},{},{}]

for info, r in zip(map_info, map_range):
    for line in info:
        d_start_range = line[0]
        s_start_range = line[1]
        range_length = line[2]
        offset = d_start_range - s_start_range
        r[(s_start_range, s_start_range+range_length -1)] = offset
#If number in range add offset
def print_ranges(map_range):
    for x in map_range:
        print(x)
print_ranges(map_range)



i = 1
lowest_values = []
for seed in seed_ranges:
    list_of_ranges = [seed] #Start with the seed range
    for map in map_range:
        list_of_temporary_ranges = []
        for s in list_of_ranges:
            seed_start, seed_stop = s[0], s[1]

            outside = True
            for range, offset in map.items():
                map_start, map_stop = range[0], range[1]
                #------------|------|------------
                #----------|----------|----------
                if map_start <= seed_start and map_stop >= seed_stop: #Sum the offset on the start and stop of the range
                    list_of_temporary_ranges.append((seed_start+offset, seed_stop+offset))
                    outside = False

                #--------|--------------|--------
                #----------|----------|----------
                elif seed_start < map_start and seed_stop > map_stop: #Three new ranges are made
                    list_of_temporary_ranges.append((seed_start, map_start-1)) #Range smaller than start up to start
                    list_of_temporary_ranges.append((map_start+offset, map_stop+offset)) #Range in the map range
                    list_of_temporary_ranges.append((map_stop+1, seed_stop)) #Range larger than map stop up to seed stop
                    outside = False

                #-------|----------|-------------
                #----------|----------|----------
                elif map_start > seed_start and seed_stop > map_start and seed_stop < map_stop: # Two new ranges are made
                    list_of_temporary_ranges.append((seed_start, map_start-1)) #Range smaller than start up to start
                    list_of_temporary_ranges.append((map_start+offset, seed_stop+offset)) #Range in the map range
                    outside = False

                #-------------|----------|-------
                #----------|----------|----------
                elif map_start < seed_start and seed_start < map_stop and map_stop < seed_stop:
                    list_of_temporary_ranges.append((seed_start+offset, map_stop+offset)) #Range smaller than start up to start
                    list_of_temporary_ranges.append((map_stop+1, seed_stop)) #Range smaller than start up to start
                    outside = False

            if outside:
                #------------------------|----|--
                #----------|----------|----------
                #or
                #--|----|------------------------
                #----------|----------|----------
                list_of_temporary_ranges.append((seed_start, seed_stop)) #Range smaller than start up to start

        print(list_of_temporary_ranges)
        list_of_ranges = list_of_temporary_ranges
        
    
    print(list_of_ranges)
    current_lowest_value = 10**30
    for range in list_of_ranges:
        if range[0] < current_lowest_value: #The range will always have the lowest value on the start
            current_lowest_value = range[0]
            
    print(current_lowest_value)
    lowest_values.append(current_lowest_value)
print(lowest_values)
print(min(lowest_values))
                
