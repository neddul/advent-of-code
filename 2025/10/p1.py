
from collections import defaultdict
with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

machine_rows = []

for row in rows:
    row = row.split()
    machine = row[0]
    joltage = row[-1]
    buttons = row[1:-1]

    machine_number = []
    for x in machine:
        if x == '.':
            machine_number.append(0)
        elif x == '#':
            machine_number.append(1)
        else:
            pass

    new_buttons = []
    for button in buttons:
        # print(b'utton)

        my_lst = []
        for x in button:
            # print(x)
            if x.isdigit():
                my_lst.append(int(x))
        new_buttons.append(tuple(my_lst))



    machine_rows.append((machine_number, new_buttons, joltage))

def push_button(button, machine):
    for index in list(button):
        if machine[index] == 0:
            machine[index] = 1
        else:
            machine[index] = 0
    return machine

def simulate(machine, buttons):
    for button in buttons:
        machine = push_button(button, machine)
    return machine

counter = 0

for machine, buttons, _ in machine_rows:
    result = []
    for value in buttons:
        new_combinations = [[value]]

        for combination in result:
            new_combinations.append(combination + [value])

        result.extend(new_combinations)

    combination_result = defaultdict(list)
    for combination in result:
        starting_state = [0]*len(machine)
        simulation_result = simulate(starting_state, combination)
        if simulation_result == machine:
            
            combination_result[len(combination)] = combination
            
    counter += min(combination_result.keys())

print(counter)