with open("input_test2.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
print(rows)


rows = [x.split("do()") for x in rows]

print(rows)
rows = [item for sublist in rows for item in sublist]
print(rows)

rows = [x.split("don't()") for x in rows]

print(rows)
rows = [item for sublist in rows for item in sublist]
print(rows)