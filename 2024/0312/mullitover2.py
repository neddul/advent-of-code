with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [x.split("mul(") for x in rows]
rows = [item for sublist in rows for item in sublist]
rows = [x.split(")") for x in rows]
rows = [item for sublist in rows for item in sublist]
rows = [x.split(",") for x in rows]

my_sum = 0
def check_stop(row):
    for r in row:
        if "don't(" in r:
            return "dont"
        if "do(" in r:
            return "do"
    return False

stopcon = False
for row in rows:
    check = check_stop(row)    
    if "do" == check:
        stopcon = False
    elif "dont" == check:
        stopcon = True
    else:
        None
    
    if len(row) == 2:
        if row[0].isdigit() and row[1].isdigit() and not stopcon:
            my_sum+= int(row[0]) * int(row[1])

print(my_sum)
