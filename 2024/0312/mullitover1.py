with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [x.split("mul(") for x in rows]
rows = [item for sublist in rows for item in sublist]
rows = [x.split(")") for x in rows]
rows = [item for sublist in rows for item in sublist]
rows = [x.split(",") for x in rows]

my_sum = 0

for row in rows:
    if len(row) == 2:
        if row[0].isdigit() and row[1].isdigit():
            my_sum+= int(row[0]) * int(row[1])

print(my_sum)
