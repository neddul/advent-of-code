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

def rotate_cell(cell):
    list_of_numbs = []
    for i in range(len(cell[0])):
        string_numb = ""
        for numb in cell:
            string_numb += numb[-(i+1)]    
        string_numb = string_numb.replace(" ", "")
        if string_numb:
            list_of_numbs.append(int(string_numb))
    return list_of_numbs

def sum_cells(numbers, op):
    numbers = [int(x) for x in numbers]
    if op == '*':
        p = 1
        for numb in numbers:
            p *= numb
        return p
    else:
        return sum(numbers)

p1 = 0
p2 = 0
for (cell, op) in cells:
    p1 += sum_cells(cell, op)
    p2 += sum_cells(rotate_cell(cell), op)
    
print(p1)
print(p2)
