with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')
numbers, ops = rows[:-1], rows[-1].split()
numbers = [x.split() for x in numbers]

def get_nums(index):
    list_of_numbs = []
    for numbs in numbers:
        list_of_numbs.append(int(numbs[index]))
    return list_of_numbs

p1 = 0
for i in range(len(ops)):
    numbs = get_nums(i)
    if ops[i] == '*':
        product = 1
        for numb in numbs:
            product *= numb
        p1 += product
    else:
        for numb in numbs:
            p1 += numb

print(p1)

