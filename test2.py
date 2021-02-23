import networkx as nx
import matplotlib.pyplot as plt


G3=nx.DiGraph()
f = open("SiouxFalls/SiouxFalls_flow.tntp", "r")
line = f.readline()
line = f.readline()
while len(line):
    l = line.split()
    fromnode = int(l[0])
    to = int(l[1])
    volume = float(l[2])
    cost = int(float(l[3]))
    G3.add_edge(fromnode, to, weight = cost)
    line = f.readline()
f.close()
print(G3.number_of_edges())

f = open("SiouxFalls/SiouxFalls_node.tntp", "r")
line = f.readline()
line = f.readline()
while len(line):
    line = line.strip(';')
    l = line.split()
    node = int(l[0])
    pos1 = float(l[1])
    pos2 = float(l[2])
    G3.add_node(node, pos=(pos1,pos2))
    line = f.readline()
f.close()
print(G3.number_of_nodes())
print(G3)

plt.figure(figsize=(8,12))
# The positions of each node are stored in a dictionary
node_pos=nx.get_node_attributes(G3,'pos')
# The edge weights of each arcs are stored in a dictionary
arc_weight=nx.get_edge_attributes(G3,'weight')
# Determine the shortest path
sp = nx.dijkstra_path(G3,source = 1, target = 20)
# Create a list of arcs in the shortest path using the zip command and store it in red edges
red_edges = list(zip(sp,sp[1:]))
# If the node is in the shortest path, set it to red, else set it to white color
node_col = ['white' if not node in sp else 'red' for node in G3.nodes()]
# If the edge is in the shortest path set it to red, else set it to white color
edge_col = ['black' if not edge in red_edges else 'red' for edge in G3.edges()]
# Draw the nodes
nx.draw_networkx(G3, node_pos,node_color= node_col, node_size=450)
# Draw the node labels
nx.draw_networkx_labels(G3, node_pos)
# Draw the edges
#nx.draw_networkx_edges(G3, node_pos,edge_color= edge_col)
# Draw the edge labels
nx.draw_networkx_edge_labels(G3, node_pos, edge_labels=arc_weight)
# Remove the axis
plt.axis('off')
# Show the plot
plt.show()
