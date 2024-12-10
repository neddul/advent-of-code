with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rules = {}
updates = []

# Make rules for pages
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

# Make list with ints for updates
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

p1_sum = 0
p2_sum = 0

for update in updates:
    reversed_row = list(reversed(update))
    violated, _ = check_violated(reversed_row)
    if violated:
        while(violated): 
            violated, index = check_violated(reversed_row)
            if violated:
                reversed_row = fix_row(reversed_row, index)
        p2_sum += reversed_row[len(reversed_row)//2]
                
    else: 
        p1_sum += update[len(update)//2]

print(p1_sum)
print(p2_sum)
