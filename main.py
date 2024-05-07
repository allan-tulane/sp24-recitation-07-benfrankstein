from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        cur = frontier.pop()
        for n in graph[cur]:
          if n not in result:
              result.add(n)
              frontier.add(n)
    return result





def connected(graph):
    sn = next(iter(graph))
    reach = reachable(graph,sn)
    return len(reach) == len(graph) 




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    n = set() 
    count = 0
    for node in graph:
        if node not in n:
          nV = reachable(graph, node)
          n.update(nV)
          count += 1  
    return count
