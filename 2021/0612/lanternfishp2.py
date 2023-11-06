# #Part one
with open("input.txt",'r') as f:
    data = f.read()

rows = data.split(',')
rows = [int(x) for x in rows]

arr = [0]*9

for x in rows:
    arr[x] +=1

for i in range(256):
    more = arr[0]
    arr = arr[1:] + [arr[0]]
    if more > 0:
        arr[6] += more

fish = 0
for x in arr:
    fish += x

print(fish)