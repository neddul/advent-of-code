with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rules = {}
updates = []

for i in range(len(rows)):
    if '|' in rows[i]:
        rule = rows[i].split('|')
        if int(rule[0]) in rules:
            rules[int(rule[0])].append(int(rule[1]))
        else:
            rules[int(rule[0])] = [int(rule[1])]
    else:
        updates = rows[i+1:]
        break

for i in range(len(updates)):
    update = updates[i].split(',')
    update = [int(x) for x in update]
    updates[i] = update

def check_violated(row):
    for i in range(len(row)-1):
        page = row[i]
        for page_updated_before_page in row[i+1:]:
            if page in rules:
                if page_updated_before_page in rules[page]:
                    return True, i
    return False, None

def fix_row(row, index):
    return row[:index] + row[index+1:] + [row[index]]

middle_page_number_sum = 0
fixed_sum = 0

violated_rows = []
for update in updates:
    reversed_row = list(reversed(update))
    violated, _ = check_violated(reversed_row)
    if violated:
        while(violated):
            violated, index = check_violated(reversed_row)
            if violated:
                reversed_row = fix_row(reversed_row, index)
        fixed_sum += reversed_row[len(reversed_row)//2]
                
    else: 
        middle_page_number_sum += update[len(update)//2]

print(middle_page_number_sum)
print(fixed_sum)

  