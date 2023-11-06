with open("input.txt",'r') as f:
    data = f.read()

rows = [int(x) for x in data.split(',')]

fuel = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
for i in range(max(rows)):
    crab_fuel = 0
    for x in rows:
        crab_fuel+= abs(i-x)
    if crab_fuel < fuel:
        fuel = crab_fuel
    else:
        break

print(fuel)
    