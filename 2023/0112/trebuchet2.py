with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

def check_if_word_number(c):
    x = c[:3]
    if x == "one":
        return "1"
    if x == "two":
        return "2"
    if x == "six":
        return "6"
    x = c[:4]
    if x == "four":
        return "4"
    if x == "five":
        return "5"
    if x == "nine":
        return "9"
    x = c[:5]
    if x == "three":
        return "3"
    if x == "eight":
        return "8"
    if x == "seven":
        return "7"
    return ""

number_sum = 0
for row in rows:
    values = ""
    for i in range(len(row)) :
        if row[i].isdigit():
            values +=row[i]
        c = check_if_word_number(row[i:i+5])
        if c.isdigit():
            values +=c
        
    if len(values) > 1:
        values = values[0] + values[-1]
    else:
        values = values[0] + values[0]
    number_sum += int(values)

print(number_sum)