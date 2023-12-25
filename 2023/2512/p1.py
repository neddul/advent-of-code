with open("input.txt",'r') as f:     data = f.read().split('\n')

import networkx as nx
import random

G = nx.Graph()
for x in data: 
    components = x.split() 
    for i in range(1, len(components)):
        G.add_edge(components[0][:3], components[i], capacity=1)

components = list(G.nodes())
while True:
    print(len(components))
    a, b = random.choices(components, k=2)
    if a != b:
        cut, clusters = nx.minimum_cut(G, a, b)
        if cut == 3:
            print(len(clusters[0]) *  len(clusters[1]))
            break