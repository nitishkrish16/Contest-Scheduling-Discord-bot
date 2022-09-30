# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 16:22:08 2022

@author: 21pt40
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import networkx as nx
def mex(l):
    n=[*range(1,max(l))]
    for i in l:
        if i in n:
            n.remove(i)
    return (min(n))

def color_vertex(g):
    colors = [1, 2, 3, 4]
    available = []
    if len(list(g.nodes))==0:
        return
    for i in g.nodes:
       # a=[g.nodes[x]['color'] if g.nodes[x]['color']!=None for x in g.adj[i] ]
        a = list(filter(lambda x:  g.nodes[x]['color']!=None, g.nodes))
        if len(a)==0:
            g.nodes[i]['color']=colors[0]
        else:
            g.nodes[i]['color']=mex(a)
            
        
G = nx.Graph()
G.add_nodes_from([

    (1, {"color": None}),
    (2, {"color": None}),
    (3, {"color": None}),
    (4, {"color": None}),
    (5, {"color":None}),

])
G.add_edges_from([(3,1),(3,2),(3,4),(3,5)])
color_vertex(G)
nx.draw(G)
