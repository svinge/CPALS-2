from astar import *
from node import *
from node_gui import *
import numpy as np


def haversine_distance(lat1, lon1, lat2, lon2):
   r = 6371
   phi1 = np.radians(lat1)
   phi2 = np.radians(lat2)
   delta_phi = np.radians(lat2 - lat1)
   delta_lambda = np.radians(lon2 - lon1)
   a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) *   np.sin(delta_lambda / 2)**2
   res = r * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
   return np.round(res, 2)





dist = haversine_distance(1,2,3,4)
#print(dist)

'''adjacency_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5), ('A',1)],
    'C': [('D', 12)]
}
graph1 = Graph(adjacency_list)
graph1.a_star_algorithm('A', 'D')'''

positions = [(3,11),(5,11),(5,7), (4,7), (1,7), (4,5),(8,7), (8,5),(12,7),(12,10), (20,10), (20,8),(20,6),(20,4),(16,4),(16,6),(16,8)]

network = Network()

n = 1
for i in positions:
    network.addNode(n, i)
    n += 1


network.addEdge(1, 2, 5)
network.addEdge(2, 3, 5)
network.addEdge(3, 4, 5)
network.addEdge(4, 5, 5)
network.addEdge(4, 6, 5)
network.addEdge(3, 7, 5)
network.addEdge(7, 8, 5)
network.addEdge(7, 9, 5)
network.addEdge(9, 10, 5)
network.addEdge(10, 11, 5)
network.addEdge(11, 12, 5)
network.addEdge(12, 13, 5)
network.addEdge(13, 14, 5)
network.addEdge(12, 17, 5)
network.addEdge(13, 16, 5)
network.addEdge(14, 15, 5)
network.addEdge(2, 10, 50)

network.showPlot()
