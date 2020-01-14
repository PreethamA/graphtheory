#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

Domination Reliability Polynomial
using theorem 5.1 in the  Reference:Domination Reliability-Klaus Dohmen and Peter Tittmann
'''

import itertools

import networkx as nx

import sympy
import time	
p = sympy.symbols('p')


def combi(G_vertices):
    '''
    function to create a combination of vertices
    using the list of vertices V(G)

    ''' 	
    # empty list of combination of vertices
    combi_vertices=[]
    # for loop to generate the combination of vertices iterating the list of vertices V(G) 
    for i in range(1,len(G_vertices)+1):
        p=list(itertools.combinations(G_vertices,i))
        combi_vertices.extend(p)

    return combi_vertices    



def polynomial(combi_vertices,G,G_vertices):
    '''
    Function to develop dominant reliability polynomial
    using combination of vertices ,graph G and vertices list of graph V(G)  
    ''' 	
    # polynomial intialization  
    ply1=0
    l=[]
    # printing the number of combinations of vertices  
    print('number of combinations of vertices:',len(combi_vertices))
    # loop for iterating each combination of vertices 
    for k in range(0,len(combi_vertices)):
        
        each_combi=list(combi_vertices[k])
        

        l2=[]
        #  for loop to find each combination of vertex is equal to closed neighbhourhood of the J 
        for i in range(0,len(each_combi)):
        

            # get neighbhourhood of each combination of vertex in the graph
            c=nx.all_neighbors(G,combi_vertices[k][i])
        
            l1=list(c)
        
             
            # create a list of neighbhourhood of each combination of vertex in the graph J
            c33=[combi_vertices[k][i]]
        
            #closed neighbhourhood of each combination of vertex in the graph J
	        l2.extend(l1)
            l2.extend(c33)
        # if closed neighbhourhood of the J is subset of vertices of graph V(G) then generate polynomial equation     
        if set(l2)==set(G_vertices):
            # list of all 
            l.extend([combi_vertices[k]])
            len_J=len(combi_vertices[k])
                
            # polynomial equation if the closed neighbhourhood of the J is subset of vertices of graph V(G)
            ply=(p**len_J)*((1-p)**(len(G_vertices)-len_J))
            # summation of all   polynomial equation       
            ply1=ply1+ply
        
    return ply1    

'''
H = nx.Graph()
    
H.add_nodes_from(['a','b','c','d','e','f','g'])
H.add_edges_from([('a','b'),('c','d'),('d','e'),('b','f'),('c','g')])
'''
#H=nx.complete_bipartite_graph(2,3)

#H=nx.petersen_graph()
#H=nx.complete_graph(7)
#H=nx.tetrahedral_graph()

#H=nx.cycle_graph(4)
#H=nx.star_graph(10)
#H=nx.empty_graph(10)

#H=nx.path_graph(6)

def main():
   # start time 
   time_start = time.time()

  	
   # graph
   G = nx.Graph()
   # add vertices 
   G.add_nodes_from(['a','b','c','d','e','f','g'])
   # add edges	
   G.add_edges_from([('a','b'),('c','d'),('d','e'),('b','f'),('c','g')])
  	
   
   # create a list for vertices of graph G 		
   G_vertices=G.nodes()
   # print the list of vertices
   print("Graph G vertices v(G):\n",G_vertices)
   # create a list for edges of graph G	
   G_edges=G.edges()
   # print the list of edges
   print("Graph G edges E(G):\n",G_edges)
   # pass the vertices list V(G) to create combinations of vertices   	
   combi_vertices=combi(G_vertices)
    # passing the combinations of vertices ,Graph G, vertices list V(G) to calculate the dominant reliability polynomial 	
   ply1=polynomial(combi_vertices,G,G_vertices)
   # print the Dominant Reliability Polynomial	
   print("Dominant Reliability Polynomial of graph G:\n",sympy.simplify(ply1))
   # printing computational time  	
   print("computational time:%s seconds"%(time.time() - time_start)) 	   
   return 0

if __name__ == "__main__":
   main()	



