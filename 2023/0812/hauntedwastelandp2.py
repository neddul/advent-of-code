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

starting_nodes = []
for k in node_network.keys():
    if k[2] == 'A':
        starting_nodes.append(k)
steps_needed = []
for node in starting_nodes:
    step_counter = 0
    key = node
    while key[2] != 'Z':
        for step in steps:
            key = node_network[key][step]
            step_counter+=1
    steps_needed.append(step_counter)

def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

factors = []
for num in steps_needed:
    factors = factors + prime_factorization(num)
factors = list(set(factors))

sum = 1
for n in factors:
    sum*=n
print(sum)