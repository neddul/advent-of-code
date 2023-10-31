file = open("input.txt")
movements = file.readlines()
file.close()

movements = [s.strip() for s in movements]
movements = [s.split() for s in movements]

horizontal = 0
depth = 0
aim = 0

up      = {"up"}
down    = {"down"}

for [movement, x] in movements:
    if movement in up:
        aim -= int(x)
    elif movement in down:
        aim += int(x)
    else:
        horizontal += int(x)
        depth += aim*int(x)

print(horizontal)
print(depth)

location = horizontal*depth
print(location)
