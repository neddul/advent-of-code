with open("input.txt",'r') as f:
    data = f.read()
rows = data.split('\n')

steps = rows[0]
node_network = rows[2:]
node_network_data = [x.split(' = ') for x in node_network]
steps = [0 if x == 'L' else 1 for x in steps]

node_network = {}
for node in node_network_data:
    node_network[node[0]] = (node[1][1:4], node[1][6:9])

current_key = 'AAA'
goal_key = 'ZZZ'

step_counter = 0
while current_key != goal_key:
    for step in steps:
        current_key = node_network[current_key][step]
        step_counter+=1

print(step_counter)

