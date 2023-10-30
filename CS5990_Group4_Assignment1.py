#from networkx.algorithms import community
#from operator import itemgetter
import matplotlib
matplotlib.use('TkAgg',force=True)
from matplotlib import pyplot as plt
import networkx as nx
import csv


def Watts_Strogatz(V, c, B):
    '''
        Require: Number of nodes |V|, mean degree c, parameter B
            1: return A small-world graph G(V,E)
            2: G = A regular ring lattice with |V| nodes and degree c
            3: for node vi (starting from v1), and all edges e(vi,vj), i < j do
            4:  vk = Select a node from V uniformly at random.
            5:  if rewiring e(vi; vj) to e(vi; vk) does not create loops in the graph or
                multiple edges between vi and vk then
            6:  rewire e(vi; vj) with probability B: E = E-{e(vi,vj)}, E = E U {e(vi; vk)};
            7:  end if
            8: end for
            9: Return G(V,E)
    '''



    return


def Barabasi_Albert():
    '''
        Require: Graph G(V0; E0), where jV0j = m0 and dv  1 8 v 2 V0, number of expected connections m  m0, time to run the algorithm t
            1: return A scale-free network
            2: //Initial graph with m0 nodes with degrees at least 1
            3: G(V,E) = G(V0,E0);
            4: for 1 to t do
            5:  V = V [ fvig; // add new node vi
            6:  while di , m do
            7:      Connect vi to a random node vj 2 V, i , j ( i.e., E = E [ {e(vi,vj)} )
                    with probability P(vj) = dj / E dk
            8:  end while
            9: end for
            10: Return G(V; E)
    '''
    return


def load_data(filename,print=False):
    if filename == 'com-amazon.ungraph.txt':
        with open('com-amazon.ungraph.txt') as fin, open('com-amazon.ungraph(fixed).txt', 'w') as fout:
            for line in fin:
                fout.write(line.replace('\t', ','))
        fin.close()
        fout.close()
        filename = 'com-amazon.ungraph(fixed).txt'

    with open(filename, 'r') as nodecsv:
        nodereader = csv.reader(nodecsv)
        nodes = [n for n in nodereader][1:]

    node_names = [n[0] for n in nodes]
    #node_names = list(set(node_names))

    with open(filename, 'r') as edgecsv:
        edgereader = csv.reader(edgecsv)
        edges = [tuple(e) for e in edgereader][1:]
    
    if print:
        print('Nodes:'+str(len(node_names)))
        print('Edges:'+str(len(edges)))

    return node_names, edges


def make_graph(node_names, edges):
    G=nx.Graph()
    G.add_nodes_from(node_names)
    G.add_edges_from(edges)
    return G


def disp_graph(G):
    nx.draw(G)
    plt.show()
    return


def print_table(ON_amazon, ON_twitch, WS, BA):
    '''
    | ------------------------------------------------------------------------------------------------------------------------------------------- |
    |                         Original Network                                |          Watts-Strogatz         |         Barabasi-Albert         |
    | ----------------------------------------------------------------------- | ------------------------------- | ------------------------------- |
    | Network         |   Size  |  Avg Deg  |   Avg Path Len  |  Clust Coeff  |   Avg Path Len  |  Clust Coeff  |   Avg Path Len  |  Clust Coeff  | 
    | Com-Amazon      |         |           |                 |               |                 |               |                 |               |
    | Twitch Gamers   |         |           |                 |               |                 |               |                 |               |
    | ------------------------------------------------------------------------------------------------------------------------------------------- |
    '''
    t = [['', 'Original Network', 'Watts-Strogatz', 'Barabasi-Albert'],
         ['Network', 'Size', 'Average Degree', 'Average Path Length', 'Clustering Coefficient', 'Average Path Length', 'Clustering Coefficient', 'Average Path Length', 'Clustering Coefficient'],
         ['Com-Amazon', ON_amazon.size(), nx.average_degree_connectivity(ON_amazon), nx.average_shortest_path_length(ON_amazon), nx.average_clustering(ON_amazon)],
         ['Twitch Gamers', ON_twitch.size(), nx.average_degree_connectivity(ON_twitch), nx.average_shortest_path_length(ON_twitch), nx.average_clustering(ON_twitch)]]

    print(t)
    return


def main(print_status=True):
    '''
    Important: The network in each of these data sets may contain multiple components. 
    You should extract the largest connected component and simulate this component using the network model implementation.
    '''
    print('CS5990 - Team 4 - Group Assignment 1\nGabriel Alfredo Siguenza, Alec Gotts, Jun Ho Ha, Ardavan Sherafat\n')

    if print_status : print('Loading "large_twitch_edges.csv" data')
    node_names, edges = load_data('large_twitch_edges.csv')
    if print_status : print('Making "large_twitch_edges.csv" graph')
    Graph_twitch = make_graph(node_names, edges)

    if print_status : print('Loading "com-amazon.ungraph.txt" data')
    node_names, edges = load_data('com-amazon.ungraph.txt')
    if print_status : print('Making "com-amazon.ungraph.txt" graph')
    Graph_amazon = make_graph(node_names, edges)

    if print_status : print('Making Watts-Strogatz (4.1) graph')
    Graph_WS = Watts_Strogatz(V=100000, c=10, B=1)
    if print_status : print('Making Barabasi-Albert (4.2) graph')
    Graph_BA = Barabasi_Albert()

    #print_table(Graph_amazon, Graph_twitch, Graph_WS, Graph_BA)
    input('Press any key to continue...')
    return


if __name__ == "__main__":
    main()