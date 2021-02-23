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
        self.closest = {'id': 99, 'pos': (99,99), 'distance': []}
        self.sp = []
        self.x = 0
        self.y = 0

    def updatePlot(self):

        plt.clf()

        #fig = plt.figure(figsize=(8,12))
        try:
            self.node_pos=nx.get_node_attributes(self.G ,'pos')
            arc_weight=nx.get_edge_attributes(self.G,'weight')
            self.sp = nx.dijkstra_path(self.G, source = 0, target = 14)
            self.getClosest()
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
    def mouse_move(self, event):

        d = 0

        self.x, self.y = event.xdata, event.ydata
        self.G.nodes[0]['pos'] = (self.x,self.y)


        try:

            for i , pos in self.G.nodes.items():
                pos = pos['pos']
                #print(i, pos)

                dist = (abs(self.x-pos[0]),abs(self.y-pos[1]))
                tot_dist = dist[0]+dist[1]
                #print(i , tot_dist)
                dist2 = (abs(self.x-self.closest['pos'][0]),abs(self.y-self.closest['pos'][1]))
                tot_dist2 = dist2[0]+dist2[1]
                self.closest['distance'].append(tot_dist2)

                if tot_dist < tot_dist2 and i != 0:
                    self.closest['pos'] = pos
                    self.closest['id'] = i
                    self.closest['distance'] = []
                    d = round(tot_dist, 2)


            for a,b in self.G.edges:
                if a == 0:
                    try:
                        self.G.remove_edge(0,b)
                    except:
                        pass

            self.addEdge(0,self.closest['id'], d)

            self.updatePlot()
        except:
            pass





    def getClosest(self):

        try:
            pos = self.closest['pos']
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
