file = open("input.txt")
readings = file.readlines()
file.close()

readings = [s.strip() for s in readings]

gamma = ""
eps = ""

for i in range(len(readings[0])):
    ones = 0
    zeroes = 0
    for stream in readings:
        if stream[i] == "1":
            ones += 1
        else:
            zeroes +=1

    if ones > zeroes:
        gamma+= "1"
        eps+= "0"
    else:
        gamma+= "0"
        eps+= "1"

gamma   = int(gamma, 2)
eps     = int(eps, 2)

print(gamma)
print(eps)

power_consumption = gamma*eps
print(power_consumption)