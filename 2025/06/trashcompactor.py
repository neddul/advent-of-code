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

def sum_cells(numbers, op):
    if op == '*':
        p = 1
        for numb in numbers:
            p *= numb
        return p
    else:
        return sum(numbers)

def get_nums(numbers, p2):
    list_of_numbs = []
    if p2:
        for i in range(len(numbers[0])):
            string_numb = ""
            for numb in numbers:
                string_numb += numb[-(i+1)]    
            string_numb = string_numb.replace(" ", "")
            if string_numb:
                list_of_numbs.append(int(string_numb))
    else:
        for number in numbers:
            list_of_numbs.append(int(number))

    return list_of_numbs

p1 = 0
p2 = 0
for (cell, op) in cells:
    p1 += sum_cells(get_nums(cell, False), op)
    p2 += sum_cells(get_nums(cell, True), op)
    
print(p1)
print(p2)
