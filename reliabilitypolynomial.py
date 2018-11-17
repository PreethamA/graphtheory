import networkx as nx
import random
import sympy

p = sympy.symbols('p')

def get_rand_edges(g, n):
    visited = set()
    results = []
    edges = random.sample(g.edges(), n)

    for edge in edges:
        if edge[0] in visited or edge[1] in visited:
            continue
        results.append(edge)

        if len(results) == n:
            break
        visited.update(edge)
	
    return results

def recursion(H):
    if not nx.is_connected(H):
       return sympy.Poly(0, p)
    
    if len(H.edges()) > 0:
       print('no of edges',len(H.edges()))
       e=get_rand_edges(H, 1)
       print('random edge:',e)
       contracted = nx.contracted_edge(H, e[0], self_loops=False)
       print('H contracted edge:',contracted.edges())
    
       H.remove_edge(*e[0])
       print('H removed edge:',H.edges())
       
       s = sympy.Poly(p)*recursion(contracted) + sympy.Poly(1-p)*recursion(H)
      
       return s
    return sympy.Poly(1, p)







#H=nx.petersen_graph()
#k=nx.tetrahedral_graph()
#k=nx.stochastic_graph(3)
#H = nx.MultiGraph(k)

H=nx.path_graph(6)
#H=nx.cycle_graph(10)
#H=nx.ladder_graph(20)
#H=nx.star_graph(10)
print('H :',H.edges)
print(sympy.simplify(recursion(H)))

