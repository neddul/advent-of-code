with open("input.txt",'r') as f:
    data = f.read()
data = [int(x) for x in data]

spaces = []
number = []

def create_block(inputdata):
    block = []
    is_id = True
    curr_id = 0
    for x in inputdata:
        if is_id:
            for _ in range(x):
                number.append(len(block))
                block.append(curr_id)
            curr_id +=1
            is_id = False
        else:
            for _ in range(x):
                spaces.append(len(block))
                block.append('.')
            is_id = True
    return block

def move_to_left_in_block(block):
    for space_index, number_index in zip(spaces, list(reversed(number))):
        if space_index < number_index:
            block[space_index] = block[number_index]
            block[number_index] = '.'
    
    return block

def block_sum(block):
    my_sum = 0
    i = 0
    for x in block:
        if x != '.' :
            my_sum += i*int(x)
        i +=1
    return my_sum

block = create_block(data)
block = move_to_left_in_block(block)

print(block_sum(block))
