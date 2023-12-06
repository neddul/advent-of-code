with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def accelerate(time, goal_length):
    distance_covered = []
    for i in range(time):
        distance = i*(time-i)
        distance_covered.append(distance)
    
    distance_covered = [x for x in distance_covered if x > goal_length]
    return len(distance_covered)

a, b, c, d = accelerate(44, 208), accelerate(80, 1581), accelerate(65, 1050), accelerate(72, 1102)
g = a*b*c*d
print(g) #P1
print(accelerate(44806572, 208158110501102)) #P2