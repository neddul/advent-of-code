with open("input_test.txt",'r') as f:
    data = f.read()

rows = data.split('\n')

print(rows)

openers = []

closer_points = {
    ')' : 3,
    ']' : 57,
    '}' : 1197,
    '>' : 25137
}

closers = set(list(closer_points.keys()))

openers = {'(', '[', '{', '<'}

illegal_closes = 0

opener_list = []

corresponding_list = {
    '(' : ')',
    '[' : ']',
    '{' : '}',
    '<' : '>'
}

for row in rows:
    for c in row:
        print(c)
        if c in openers:
            opener_list.append(c)
        elif len(opener_list) == 0:
            illegal_closes += closer_points[c]
        elif opener_list[-1] != corresponding_list[opener_list[-1]]:
            illegal_closes += closer_points[c]
        else:
            opener_list.pop()

print(illegal_closes)



