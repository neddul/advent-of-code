with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

closer_points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

corresponding_list = {
    ')' : '(',
    ']' : '[',
    '}' : '{',
    '>' : '<'
}

corresponding_list_2 = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

closers = set(list(closer_points.keys()))
openers = set(list(corresponding_list.values()))

illegal_closes = 0
stack = []

incomplete_rows = []

for row in rows:
    incomplete_rows.append(row)
    for c in row:
        if c in openers:
            stack.append(c)
        else:
            if len(stack) == 0:
                illegal_closes += closer_points[c]
                incomplete_rows.pop()
                break
            elif stack[-1] != corresponding_list[c]:
                illegal_closes += closer_points[c]
                incomplete_rows.pop()
                break
            else:
                stack.pop()
    stack = []

stack = []
closer_stack = []

closer_points = {
    ')' : 1,
    ']' : 2,
    '}' : 3,
    '>' : 4
}

number_sum = []
for row in incomplete_rows:
    for c in row:
        if c in openers:
            stack.append(c)
        else:
            stack.pop()

    for c in list(reversed(stack)):
        closer_stack.append(corresponding_list_2[c])
    row_sum = 0
    for c in closer_stack:
        row_sum*=5
        row_sum+=closer_points[c]
    stack=[]
    closer_stack=[]
    number_sum.append(row_sum)


number_sum = sorted(number_sum)
middle = int(len(number_sum)/2)
print(number_sum[middle])