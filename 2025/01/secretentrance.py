with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

number = 50
counter = 0

for rotate in rows:
    direction = rotate[0]
    nudges = int(rotate[1:])

    number = number + nudges if direction == "R" else number - nudges
    number = number % 100

    if number == 0:
        counter += 1

print(counter)

