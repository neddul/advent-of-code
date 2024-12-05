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

middle_page_number_sum = 0
for update in updates:
    violated = False
    reversed_list = list(reversed(update))
    for i in range(len(reversed_list)-1):
        page = reversed_list[i]
        for page_updated_before_page in reversed_list[i+1:]:
            if page in rules:
                if page_updated_before_page in rules[page]:
                    violated = True
                    
        if violated:
            break
        
    if not violated:
        middle_page_number_sum += update[len(update)//2]
        
print(middle_page_number_sum)
