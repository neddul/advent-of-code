# #Part one
with open("input_test.txt",'r') as f:
    data = f.read()
print(data)

rows = data.split(',')
rows = [int(x) for x in rows]
print(rows)

def update_fish(items):
    for i in range(len(items)):
        if items[i] == 0:
            items[i] = 6
            items.append(8)
        else:
            items[i] -=1
    return items

def simulate_days_for_fish(cycle, days):
    fishes = [cycle]
    for i in range(days):
        fishes = update_fish(fishes)
        print(i)
    
    return len(fishes)
    
occurances = {}
for x in rows:
    if x not in occurances:
        occurances[x] = 1
    else:
        occurances[x] += 1

print(occurances)

total_fishes = 0
for cycle, times in occurances.items():
    fishes = simulate_days_for_fish(cycle, 80)
    total_fishes += fishes*times

print(total_fishes)