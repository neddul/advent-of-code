with open("input.txt",'r') as f:
    data = f.read()

rows = [x for x in data.split('\n')]
segment = []
digits = []
for x in rows:
    row = x.split(' | ')
    segment.append(row[0].split(' ')[:10])
    digits.append(row[1].split(' '))

def superior_replace(chars, string):
    for c in chars:
        string = string.replace(str(c), "")
    return string

def parse_segment(segment):
    segment = [''.join(sorted(s)) for s in segment]
    digits = ['']*10
    for s in segment:
        if len(s) == 2:
            digits[1] = s
        if len(s) == 3:
            digits[7] = s
        if len(s) == 4:
            digits[4] = s
        if len(s) == 7:
            digits[8] = s
    for s in segment:
        if len(s) == 6 and len(superior_replace(digits[4], s)) == 2:
            digits[9] = s
        if len(s) == 6 and not (digits[1][0] in s and digits[1][1] in s):
            digits[6] = s
        if len(s) == 6 and not s == digits[6] and not s == digits[9]:
            digits[0] = s
        if len(superior_replace(digits[1], s)) == 3:
            digits[3] = s
        if len(s) == 5 and len(superior_replace(digits[7], superior_replace(digits[4], s))) == 2:
            digits[2] = s
        if len(s) == 5 and len(superior_replace(digits[7], superior_replace(digits[4], s))) == 1:
            digits[5] = s    

    return digits                

numbers = {
    0:0,
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0
}

for x,y in zip(segment, digits):
    code = parse_segment(x)
    for digit in y:
        digit = ''.join(sorted(digit))
        for i in range(len(code)):
            if code[i] == digit:
                numbers[i] +=1


print(numbers)

