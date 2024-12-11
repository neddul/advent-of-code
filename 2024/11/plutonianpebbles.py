with open("input.txt",'r') as f:
    data = f.read()

from collections import defaultdict

def create_new_stones(stones):
    new_stones = defaultdict(int)
    for stone, v in stones.items():
        if int(stone) == 0:
            new_stones["1"] += v
        elif len(stone) % 2 == 0:
            new_stone1, new_stone2 = stone[:len(stone)//2], str(int(stone[len(stone) // 2:]))
            new_stones[new_stone1] += v
            new_stones[new_stone2] += v
        else:
            new_stone = str(int(stone)*2024)
            new_stones[new_stone] += v
    return new_stones

stones = defaultdict(int, {x: 1 for x in data.split()})
for _ in range(25):
    stones = create_new_stones(stones)

print(sum(stones.values()))   

stones = defaultdict(int, {x: 1 for x in data.split()})
for _ in range(75):
    stones = create_new_stones(stones)

print(sum(stones.values()))   
