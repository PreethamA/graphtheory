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
'''
def check_list(H,combi_nodes,H_nodes):
    #p=H.copy()
    c=[]
    l=[]
    print("number of J elements:",len(combi_nodes))
    print("J elements:\n",combi_nodes)
    for i in range(0,len(combi_nodes)):
        print('J element:',combi_nodes[i])
        #print(i)
        if len(combi_nodes[i])==1:
            print('J element:',combi_nodes[i][0])
            
            c=nx.all_neighbors(H,combi_nodes[i][0])
            l1=list(c)
            print("nH(J):",l1)
            c33=[combi_nodes[i][0]]
            #print(c33)
            l1.extend(c33)
            print('nH[J]:',l1)
            
            if set(l1)==set(H_nodes):
                l.extend([combi_nodes[i][0]])
                print('nH[J]==H(v) element of J:',l) 
                #single_vertex=len(l)
                #print(single_vertex)
            #l12=cmp(l1, H_nodes)
               
            
            
        else:
            print('J element:',combi_nodes[i])
            lwe=[]
            for k in range(0,len(combi_nodes[i])):
                print('J element in tuple:',combi_nodes[i][k])
                c1=nx.all_neighbors(H,combi_nodes[i][k])
                l11=list(c1)
                
                c331=[combi_nodes[i][k]]

                lwe.extend(l11)
                lwe.extend(c331)
                print('nH[J]:',lwe)
                
            if set(lwe)==set(H_nodes):
                l.extend([combi_nodes[i]])
                print('nH[J]==H(v) element of J:',l)
            
            
            
    return l


H = nx.Graph()
    
H.add_nodes_from(['a','b','c','d','e','f','g'])
H.add_edges_from([('a','b'),('c','d'),('d','e'),('b','f'),('c','g')])
'''
#H=nx.complete_bipartite_graph(2,3)
#H=nx.grid_graph(dim=[5,5])
    #H=nx.petersen_graph()
#H=nx.complete_graph(3)
    #H=nx.tetrahedral_graph()
   #k=nx.stochastic_graph(3)
#H=nx.cycle_graph(4)
    #H=nx.star_graph(10)
H=nx.empty_graph(10)

#H=nx.path_graph(3)



H_nodes=H.nodes()
print("graph H nodes:",H_nodes)

ply1=0
#a = [1,2,3,4,5]
combi_nodes=combi(H_nodes)

l=[]

print('number of combinations of vertices:',len(combi_nodes))

for k in range(0,len(combi_nodes)):
    
    each_combi=list(combi_nodes[k])
    
    print("combination:",each_combi)
    
    len_tuple=len(each_combi)
    
    print("length of combination:",len(each_combi))
    l2=[]
    for i in range(0,len(each_combi)):
        
        print('looking for the neigbour of node:',combi_nodes[k][i])
        
        c=nx.all_neighbors(H,combi_nodes[k][i])
        
        l1=list(c)
        
        print("nH(J):",l1)
        
        c33=[combi_nodes[k][i]]
        
        print(c33)
        l2.extend(l1)
        l2.extend(c33)
        
        print('nH[J]:',l2)
            
    if set(l2)==set(H_nodes):
        
        l.extend([combi_nodes[k]])
        len_J=len(combi_nodes[k])
        print(len_J)
        
        print('nH[J]==H(v) for the  elements of J:',l)
        
        ply=(p**len_J)*((1-p)**(len(H_nodes)-len_J))
        
        ply1=ply1+ply
        print("dominat reliability polynomial for the graph H")
        print(sympy.simplify(ply1))
#k=combi_nodes[3]
#print(k[1])

#se=zip(*combi_nodes)
#print(se)
#output = sum([map(list,itertools.combinations(a, i)) for i in range(len(a) + 1)], [])   
#result = list(itertools.product(a))
#print(output)
#vertices=check_list(H,combi_nodes,H_nodes)
#print(vertices)
#ly1=dominat_reliability(vertices,H_nodes)
#print(ply1)
