file = open("input.txt")
movements = file.readlines()
file.close()

movements = [s.strip() for s in movements]
movements = [s.split() for s in movements]

horizontal = 0
depth = 0

up      = {"up"}
down    = {"down"}

for [movement, x] in movements:
    if movement in up:
        depth -= int(x)
    elif movement in down:
        depth += int(x)
    else:
        horizontal += int(x)

print(horizontal)
print(depth)

location = horizontal*depth
print(location)
