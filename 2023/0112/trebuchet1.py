with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

number_sum = 0
for row in rows:
    values = ""
    for c in row:
        if c.isdigit():
            values +=c

    if len(values) > 1:
        values = values[0] + values[-1]
    else:
        values = values[0] + values[0]
    number_sum += int(values)

print(number_sum)