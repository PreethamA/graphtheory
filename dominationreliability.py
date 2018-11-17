import networkx as nx

import sympy
import mpmath

p = sympy.symbols('p')

def main(H):
    X_dominate=nx.dominating_set(H)

    v=H.nodes()
    print('number of dominate vertices: \n',len(X_dominate))
    print(' dominate vertices are : \n',X_dominate)

    firstterm=sympy.simplify((1-p)**len(v))
    #print('firstterm:',firstterm)
    secondterm= mpmath.nsum(lambda k:sympy.simplify(sympy.Mul(sympy.binomial(len(v), k),sympy.Mul((p**k)),(1-p)**(-k))), [len(X_dominate), len(v)])

    #print('secondterm:',secondterm)
    finalterm=sympy.Mul(firstterm,secondterm)
    print('Domination Reliability Polynomial of a graph H :\n',sympy.simplify(finalterm))
    return 

if __name__ == '__main__':
    '''
    H = nx.Graph()
    
    H.add_nodes_from([1,2,3,4,5,6])
    H.add_edges_from([(1,2),(2,3),(4,6),(5,6),(6,3),(2,5),(3,5),(1,3)])
    '''
    #H=nx.grid_graph(dim=[5,5])
   # H=nx.petersen_graph()
    #H=nx.complete_graph(4)
    #H=nx.tetrahedral_graph()
   #k=nx.stochastic_graph(3)
    #H=nx.cycle_graph(3)
    #H=nx.star_graph(10)
    H=nx.empty_graph(10)

    #H=nx.path_graph(3)

    if len(H.nodes())==0:
        print("\n warning: number of vertices is Zero ")
    else:

      print('Graph H nodes:\n',H.nodes())
    
    
    
    if len(H.edges())==0:
        print("\n warning: number of edges is Zero ")
    else:
        print(' Graph H edges:\n',H.edges())

#print('G :nodes:',G.nodes())
#sympy.mpmath.

main(H)

