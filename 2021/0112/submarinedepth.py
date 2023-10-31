file = open("input.txt")
readings = file.readlines()
file.close()

readings = [s.strip() for s in readings]
readings = [int(s) for s in readings]

depth_increase = 0

for i in range(len(readings)-1):
    if readings[i+1] > readings[i]:
        depth_increase += 1

print(depth_increase) 