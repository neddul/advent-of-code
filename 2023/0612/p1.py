with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

time = rows[0].split()[1:]
distance = rows[1].split()[1:]

def accelerate(time, goal_length):
    time = time+1
    for i in range(time):
        distance = i*(time-i-1)
        if distance > goal_length:
            if time % 2 == 0:
                return time - (i*2)
            else:
                return time - ((i)*2)

sum = 1
for t, d in zip(time, distance):
    a = accelerate(int(t), int(d))
    sum *= a
print(sum) #P1

print(accelerate(int(''.join(time)), int(''.join(distance)))) #P2

# 0 1 2 3 4 5 6 7
#  \           /
#   \         /
# --------------------
#     \     /
#      \   /
#       \ /