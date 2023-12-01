with open("input.txt",'r') as f:
    data = f.read()

rows2 = data.split('\n')


def is_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

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


for rows in rows2:
    values = ""
    for i in range(len(rows)) :
        if is_integer(rows[i]):
            values +=rows[i]
        if is_integer(check_if_word_number(rows[i:])):
            values +=check_if_word_number(rows[i:])
        print(values)

    if len(values) > 1:
        values = values[0] + values[-1]
    else:
        values = values[0] + values[0]
    print(values)
    data += int(values)

    


    

print(data)