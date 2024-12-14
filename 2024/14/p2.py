with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

x_axis = 101
y_axis = 103

robot_run = []

for run in rows:
    startp, startv = run.split()
    x, y = startp.replace('p=', '').split(',')
    vx, vy = startv.replace('v=', '').split(',')
    robot_run.append((int(x), int(y), int(vx), int(vy)))

def move_robot(robot_run, seconds, x_axis, y_axis):
    x, y, vx, vy = robot_run

    x += vx*seconds
    y += vy*seconds
    
    x = x % x_axis
    y = y % y_axis
    return x, y

second = 2100
while(second < 103*101):
    robot_map = []
    for y in range(y_axis):
        robot_map.append(['.']*x_axis)
    
    q1, q2, q3, q4 = 0,0,0,0
    for run in robot_run:
        x, y = move_robot(run, second, x_axis, y_axis)
        robot_map[y][x] = '#'
        if x < x_axis // 2 and y < y_axis // 2: # Q1
            q1 += 1
        elif x > x_axis // 2 and y < y_axis // 2: # Q2
            q2 += 1
        elif x < x_axis // 2 and y > y_axis // 2: # Q3
            q3 += 1
        elif x > x_axis // 2 and y > y_axis // 2: # Q4
            q4 += 1
        else:
            continue
    
    if q1 > len(robot_run)*0.44:
        for x in robot_map:
            print(x)
        print(second)
    elif q2 > len(robot_run)*0.44:
        for x in robot_map:
            print(x)
        print(second)
    elif q3 > len(robot_run)*0.44: 
        for x in robot_map:
            print(x)
        print(second)
    elif q4 > len(robot_run)*0.44:
        for x in robot_map:
            print(x)
        print(second)
    second +=1

#76, 179, 282, 385 # sida 103
#14, 115, 216, 317 # upp  101

# 7286
