with open("input.txt",'r') as f:
    data = f.read()
data = [int(x) for x in data]

spaces = dict()
files = []

def create_block(inputdata):
    block = []
    is_id = True
    curr_id = 0
    for x in inputdata:
        if is_id:
            files.append(len(block)) # Where files start
            for _ in range(x):
                block.append(curr_id)
            curr_id +=1
            is_id = False
        else:
            if x > 0:
                if x in spaces:
                    spaces[x].append(len(block))
                else:
                    spaces[x] = [len(block)]
            for _ in range(x):
                block.append('.')
            is_id = True
    return block

def try_move_entire_file(block, file_indices):
    file_len = len(file_indices)

    potential_spots = [x for x in spaces.keys() if x >= file_len]
    if len(potential_spots) > 0:
        lowest_indices = []
        for spot_size in potential_spots:
            if len(spaces[spot_size]) > 0:
                lowest_indices.append((spot_size, min(spaces[spot_size])))

        if len(lowest_indices) > 0:
            lowest_indices = sorted(lowest_indices, key=lambda x: x[1])
            spot_size, index = lowest_indices[0][0], lowest_indices[0][1]
        
            if index < file_indices[0]: #is it further left?
                for i in range(file_len):
                    block[index+i] = block[file_indices[i]]
                    block[file_indices[i]] = '.'

                spaces[spot_size].remove(index)
                new_spot_size = spot_size-file_len
                if new_spot_size > 0:
                    new_index = index + file_len
                    if new_spot_size in spaces:
                        spaces[new_spot_size].append(new_index)
                    else:
                        spaces[new_spot_size] = [new_index]
                
    return block
    

def move_files(block):
    for file_start_loc in list(reversed(files)):
        file_indices = [file_start_loc]
        i = 1
        next_index = file_start_loc + i
        while (block[next_index] == block[file_start_loc]):
            file_indices.append(next_index)
            next_index+=1
            if next_index == len(block):
                break

        block = try_move_entire_file(block, file_indices)
    return block

block = create_block(data)
block = move_files(block)

meme = 0
i = 0
for x in block:
    if x != '.' :
        meme += i*int(x)
    i +=1
print((meme))
