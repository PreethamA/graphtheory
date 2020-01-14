#!/usr/bin/env python3
# -*- coding: utf-8 -*-


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

#H=nx.complete_bipartite_graph(2,3)
#H=nx.grid_graph(dim=[5,5])
    #H=nx.petersen_graph()
#H=nx.complete_graph(3)
    #H=nx.tetrahedral_graph()
   #k=nx.stochastic_graph(3)
#H=nx.cycle_graph(4)
    #H=nx.star_graph(10)
#H=nx.empty_graph(10)

H=nx.path_graph(3)



H_nodes=H.nodes()
print("graph H nodes:",H_nodes)

ply1=0
#a = [1,2,3,4,5]
combi_nodes=combi(H_nodes)

l=[]

print('number of combinations of vertices:',len(combi_nodes))

for k in range(0,len(combi_nodes)):
    
    each_combi=list(combi_nodes[k])
    
    #print("combination:",each_combi)
    
    len_tuple=len(each_combi)
    
    #print("length of combination:",len(each_combi))
    l2=[]
    for i in range(0,len(each_combi)):
        
        #print('looking for the neigbour of node:',combi_nodes[k][i])
        
        c=nx.all_neighbors(H,combi_nodes[k][i])
        
        l1=list(c)
        
        #print("nH(J):",l1)
        
        c33=[combi_nodes[k][i]]
        
        #print(c33)
        l2.extend(l1)
        l2.extend(c33)
        
        #print('nH[J]:',l2)
            
    if set(l2)==set(H_nodes):
        
        l.extend([combi_nodes[k]])
        len_J=len(combi_nodes[k])
        #print(len_J)
        
        #print('nH[J]==H(v) for the  elements of J:',l)
        
        ply=(p**len_J)*((1-p)**(len(H_nodes)-len_J))
        
        ply1=ply1+ply
        print("dominat reliability polynomial for the graph H")
        print(sympy.simplify(ply1))

