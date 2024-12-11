with open("input.txt",'r') as f:
    data = f.read()
rows = data.split()
print(rows)

stone_list = rows

blinks = 25

def create_new_stones(stones):
    new_stones = []
    for stone in stones:
        if int(stone) == 0:
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(stone[:len(stone) // 2])
            new_stones.append(str(int(stone[len(stone) // 2:])))
        else:
            new_stones.append(str(int(stone)*2024))
    return new_stones


for i in range(blinks):
    print(i+1)
    stone_list = create_new_stones(stone_list)
        
print(len(stone_list))