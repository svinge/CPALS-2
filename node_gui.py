import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import cbook
import netgraph
import math
import numpy as np
import operator
import itertools





class Network():

    def __init__(self):
        self.G = nx.Graph()
        self.addNode(0 , (0,0))
        self.sp = []
        self.x = 0
        self.y = 0

    def updatePlot(self):

        plt.clf()

        try:
            self.node_pos=nx.get_node_attributes(self.G ,'pos')
            arc_weight=nx.get_edge_attributes(self.G,'weight')
            red_edges = list(zip(self.sp,self.sp[1:]))
            node_col = ['gray' if not node in self.sp else 'red' for node in self.G.nodes()]
            edge_col = ['black' if not edge in red_edges else 'red' for edge in self.G.edges()]
            nx.draw_networkx(self.G, self.node_pos,node_color= node_col, edge_color = edge_col, node_size=450)
            nx.draw_networkx_edge_labels(self.G, self.node_pos, edge_labels=arc_weight)
            plt.axis('off')

            plt.pause(0.0001)
            plt.show()
        #nx.draw(self.G)
        except:
            pass


    def getDistance(self, a,b):
        try:
            a = self.G.nodes(data=True)[a]['pos']
            b = self.G.nodes(data=True)[b]['pos']
            return math.sqrt((a[0]-b[0])**2+ (a[1]-b[1])**2)
        except:
            pass

    def closest_node(self, node, nodes):
        try:
            nodes = np.asarray(nodes)
            deltas = nodes - node
            dist_2 = np.einsum('ij,ij->i', deltas, deltas)
            return np.argmin(dist_2)+1
        except:
            pass

    def mouse_move(self, event):

        try:

            self.x, self.y = event.xdata, event.ydata
            self.G.nodes[0]['pos'] = (self.x,self.y)

            closest = self.closest_node(self.G.nodes[0]['pos'],list(self.node_pos.values())[1:] )

            d = round(self.getDistance(0,closest),2)

            for a,b in self.G.edges:
                if a == 0:
                    try:
                        self.G.remove_edge(0,b)
                    except:
                        pass


            self.addEdge(0,closest, d)
            self.findPath()
            self.getClosest(closest)
            self.updatePlot()

        except:
            pass


    def findPath(self):
        self.sp = nx.dijkstra_path(self.G, source = 0, target = 14)



    def getClosest(self, closest):

        try:
            pos = self.G.nodes[closest]['pos']
            nextid = self.sp[2]
            pos2 = self.G.nodes[nextid]['pos']

            ab = [pos2[0]-pos[0],pos2[1]-pos[1]]
            ba = [pos[0]-pos2[0],pos[1]-pos2[1]]

            ac = [self.x-pos[0],self.y-pos[1]]
            bc = [self.x-pos2[0],self.y-pos2[1]]


            x = np.dot(ab, ac)
            y = np.dot(ba, bc)


            if (x > 0 and y > 0):
                self.sp.pop(1)
                for a,b in self.G.edges:
                    if a == 0:
                        try:
                            self.G.remove_edge(0,b)
                        except:
                            pass

                self.addEdge(0,nextid,5)





        except:
            pass



    def addNode(self, id, pos):
        self.G.add_node(id, pos = pos)

    def addEdge(self, tx, rx, weight):
        self.G.add_edge(tx, rx, weight = weight)

    def showPlot(self):
        fig = plt.figure(figsize=(8,12))
        self.node_pos=nx.get_node_attributes(self.G ,'pos')
        arc_weight=nx.get_edge_attributes(self.G,'weight')
        nx.draw_networkx(self.G, self.node_pos,node_color= 'gray', edge_color = 'black', node_size=450)
        nx.draw_networkx_edge_labels(self.G, self.node_pos, edge_labels=arc_weight)
        plt.axis('off')



        plt.connect('motion_notify_event', self.mouse_move)
        plt.show()
        #plt.ion()
