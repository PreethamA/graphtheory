#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Domination Reliability Polynomial
using theorem 5.1 in the  Reference:Domination Reliability-Klaus Dohmen and Peter Tittmann
'''

import itertools

import networkx as nx

import sympy

p = sympy.symbols('p')


def combi(a):
    k=[]
    for i in range(1,len(a)+1):
        p=list(itertools.combinations(a,i))
        k.extend(p)
    return k    



def polynomial(combi_nodes,H,H_nodes):
    ply1=0
    l=[]

    print('number of combinations of vertices:',len(combi_nodes))

    for k in range(0,len(combi_nodes)):
        
        each_combi=list(combi_nodes[k])
        

        l2=[]
        for i in range(0,len(each_combi)):
        

            
            c=nx.all_neighbors(H,combi_nodes[k][i])
        
            l1=list(c)
        

        
            c33=[combi_nodes[k][i]]
        

            l2.extend(l1)
            l2.extend(c33)
            
        if set(l2)==set(H_nodes):
        
            l.extend([combi_nodes[k]])
            len_J=len(combi_nodes[k])
                
        
            ply=(p**len_J)*((1-p)**(len(H_nodes)-len_J))
        
            ply1=ply1+ply
        
    return ply1,l    


H = nx.Graph()
    
H.add_nodes_from(['a','b','c','d','e','f','g'])
H.add_edges_from([('a','b'),('c','d'),('d','e'),('b','f'),('c','g')])

#H=nx.complete_bipartite_graph(2,3)

#H=nx.petersen_graph()
#H=nx.complete_graph(7)
#H=nx.tetrahedral_graph()

#H=nx.cycle_graph(4)
#H=nx.star_graph(10)
#H=nx.empty_graph(10)

#H=nx.path_graph(6)



H_nodes=H.nodes()
print("graph H nodes:\n",H_nodes)

H_edges=H.edges()
print("graph H edges:\n",H_edges)
#a = [1,2,3,4,5]
combi_nodes=combi(H_nodes)
#print('combi:',combi_nodes)
ply1,l=polynomial(combi_nodes,H,H_nodes)
#print('nH[J]==H(v) for the  elements of J:\n',l)
print("Dominant Reliability PolynomiaL of graph H:\n",sympy.simplify(ply1))
