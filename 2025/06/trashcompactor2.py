with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
numbers, ops = rows[:-1], rows[-1]

ops_index = [i for i, ch in enumerate(ops) if ch in "+*"]
boundaries = ops_index + [len(ops)]

cells = []

for i in range(len(ops_index)):
    start = ops_index[i]
    end   = boundaries[i+1]
    cell = [r[start:end] for r in numbers]
    cells.append((cell, ops[ops_index[i]]))

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
