with open("input_test.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
print(rows)
# rows = [list(x) for x in rows]
# print(rows)


# roww = [x for x in roww if x == "m" or x == "u" or x == "l" or x.isdigit() or x == "(" or x == ")" or x == ","]
rows = [x.split("mul(") for x in rows]

print(rows)
rows = [item for sublist in rows for item in sublist]
print(rows)
rows = [x.split(")") for x in rows]
print(rows)
rows = [item for sublist in rows for item in sublist]
rows = [x.split(",") for x in rows]

my_sum = 0

for row in rows:
    if len(row) == 2:
        if row[0].isdigit() and row[1].isdigit():
            my_sum+= int(row[0]) * int(row[1])

print(my_sum)

# for row in rows:
    

