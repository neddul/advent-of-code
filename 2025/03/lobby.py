with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

p1 = 0
p2 = 0

def find_digit(digits, row):
    max_dig = 0
    max_dig_index = 0
    for i in range(len(row) - digits + 1):
        numb = int(row[i])
        if numb == 9:
            max_dig = numb
            max_dig_index = i
            break
        elif numb > max_dig:
            max_dig = numb
            max_dig_index = i

    return max_dig, row[max_dig_index+1:]    

for row in rows:
    list_row = list(row)
    numb = ""
    list_rowp1 = list_row
    for dig in reversed(range(1, 2 +1)):
        max_dig, list_rowp1 = find_digit(dig, list_rowp1)
        numb += str(max_dig)
    
    p1 += int(numb)

    numb = ""
    list_rowp2 = list_row
    for dig in reversed(range(1, 12 +1)):
        max_dig, list_rowp2 = find_digit(dig, list_rowp2)
        numb += str(max_dig)
    
    p2 += int(numb)

print(p1)
print(p2)
