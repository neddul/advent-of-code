with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

robot_map = []
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

x_axis = 101
y_axis = 103

q1, q2, q3, q4 = 0,0,0,0
for run in robot_run:
    x, y = move_robot(run, 100, x_axis, y_axis)
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

print(q1*q2*q3*q4)
