with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

number = 50
counter = 0
counter2 = 0


for rotate in rows:
    direction = rotate[0]
    nudges = int(rotate[1:])
    
    last_num = number
    hundreds = int(nudges / 100)

    counter2 += hundreds

    offset = nudges % 100
    number2 = number + nudges if direction == "R" else number - nudges

    number = number + offset if direction == "R" else number - offset

    if number2  % 100 == 0:
        counter += 1
    
    if number == 0:
        counter2 += 1
    else:
        if number < 0:
            number +=100
            counter2 += 1
        elif number > 99:
            number -= 100
            counter2 += 1
    
    if direction == "L" and last_num == 0:
        counter2 -= 1

    
print(counter)  
print(counter2)  
