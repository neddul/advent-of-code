with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
numbers, ops = rows[:-1], rows[-1]
ops += "+"

ops_index = []
for i in range(len(ops)):
    if ops[i] == '*' or ops[i] == '+':
        ops_index.append(i)

cells = []
prev = 0
for index in ops_index[1:]:
    cell = []
    for numb in numbers:

        cell.append(numb[prev:index])
    cells.append((cell, ops[prev]))
    prev = index

p2 = 0
for (numbs, op) in cells:
    nums = []
    for i in range(len(numbs[0])):
        string_numb = ""
        for numb in numbs:
            string_numb += numb[-(i+1)]
        string_numb = string_numb.replace(" ", "")
        if string_numb:
            nums.append(int(string_numb))
    
    p = 0
    if op == '*':
        p = 1
        for num in nums:
            p *= num
    else:
        p = sum(nums)

    p2 += p

print(p2)
    

