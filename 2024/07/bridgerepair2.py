with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

rows = [x.split() for x in rows]

def possible_eq(integers, operations):
    if len(integers) == 1:
        return integers[0]
    i = 0
    result = integers[0]
    for operation in operations:
        if operation == '+':
            result = result + integers[i+1]
        elif operation == '*':
            result = result * integers[i+1]
        else:
            result = int(str(result) + str(integers[i+1]))
        i+=1
    return result

def generate_combinations(n):
    combinations = [[]]
    for _ in range(n - 1):
        new_combinations = []
        for comb in combinations:
            new_combinations.append(comb + ['+'])
            new_combinations.append(comb + ['*'])
            new_combinations.append(comb + ['||'])

        combinations = new_combinations

    return combinations

def check_eq(start_sum, integers):
    possible_operations = generate_combinations(len(integers))
    for operations in possible_operations:
        res = possible_eq(integers, operations)
        if res == start_sum: 
            return True
    return False

bridgesum = 0
for row in rows:
    start_sum = int(row[0][:-1])
    integers = [int(x) for x in row[1:]]
    if check_eq(start_sum, integers):
        bridgesum += start_sum

print(bridgesum)
