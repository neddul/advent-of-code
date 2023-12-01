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

closers = set(list(closer_points.keys()))
openers = set(list(corresponding_list.values()))

illegal_closes = 0
stack = []


for row in rows:
    for c in row:
        if c in openers:
            stack.append(c)
        else:
            if len(stack) == 0:
                illegal_closes += closer_points[c]
                break
            elif stack[-1] != corresponding_list[c]:
                illegal_closes += closer_points[c]
                break
            else:
                stack.pop()
    stack = []


print(illegal_closes)