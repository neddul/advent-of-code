#Part two
file = open("input.txt")
readings = file.readlines()
file.close()

readings = [s.strip() for s in readings]
readings = [int(s) for s in readings]

sliding_window_readings = []

for i in range(len(readings)-2):
    combined_depth = readings[i] + readings[i+1] + readings[i+2]
    sliding_window_readings.append(combined_depth)

depth_increase = 0

for i in range(len(sliding_window_readings)-1):
    if sliding_window_readings[i+1] > sliding_window_readings[i]:
        depth_increase += 1

print(depth_increase) 