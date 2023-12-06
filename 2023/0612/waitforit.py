with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

time = rows[0].split()[1:]
distance = rows[1].split()[1:]
from math import sqrt
def accelerate(time, goal_length):
    x = int(time /2 - sqrt(time*time/4 - goal_length))
    return time - 2*x -1

sum = 1
for t, d in zip(time, distance):
    a = accelerate(int(t), int(d))
    sum *= a
print(sum) #P1
print(accelerate(int(''.join(time)), int(''.join(distance)))) #P2