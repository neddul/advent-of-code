with open("input.txt",'r') as f:
    data = f.read()
rows = data.split()

def create_new_stones(stones):
    new_stones = dict()
    for stone, v in stones.items():
        if int(stone) == 0:
            new_stone = "1"
            if new_stone in new_stones:
                new_stones[new_stone] += v
            else:
                new_stones[new_stone] = v
        elif len(stone) % 2 == 0:
            new_stone1, new_stone2 = stone[:len(stone)//2], str(int(stone[len(stone) // 2:]))
            if new_stone1 in new_stones:
                new_stones[new_stone1] += v
            else:
                new_stones[new_stone1] = v
            
            if new_stone2 in new_stones:
                new_stones[new_stone2] += v
            else:
                new_stones[new_stone2] = v
        else:
            new_stone = str(int(stone)*2024)
            if new_stone in new_stones:
                new_stones[new_stone] += v
            else:
                new_stones[new_stone] = v
    return new_stones

stones = dict([(x, 1) for x in rows])
for _ in range(25):
    stones = create_new_stones(stones)

print(sum(stones.values()))   

stones = dict([(x, 1) for x in rows])
for _ in range(75):
    stones = create_new_stones(stones)

print(sum(stones.values()))    
