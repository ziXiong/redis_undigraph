from redis_wrap import *


#-------------------edges-----------------------
def add_edge(node1, node2, system='default'):
    edges1 = get_set(node1, system=system)
    edges1.add(node1)
    edges2 = get_set(node2, system=system)
    edges2.add(node2)


def delete_edge(node1, node2, system='default'):
    edges1 = get_set(node1, system=system)
    edges1.remove(node1)
    edges2 = get_set(node2, system=system)
    edges2.remove(node2)


def has_edge(node1, node2, system='default'):
    edges1 = get_set(node1, system=system)
    edges2 = get_set(node2, system=system)
    return node1 in edges2 and node2 in edges1


# Todo: find way to balance lazy query and binary string decode.
def neighbors(node, system='default'):
    nodes = get_set(node, system=system)
    return {node.decode() for node in nodes}


#-------------------edge value--------------------
def get_edge_value(node1, node2, system='default'):
    if node1 > node2:
        edge_key = 'ev:'+node1+'_'+node2
    else:
        edge_key = 'ev:'+node2+'_'+node1
    return get_redis(system).get(edge_key).decode()


def set_edge_value(node1, node2, value, system='default'):
    if node1 > node2:
        edge_key = 'ev:'+node1+'_'+node2
    else:
        edge_key = 'ev:'+node2+'_'+node1
    return get_redis(system).set(edge_key, value)


#-------------------node value--------------------
def get_node_value(node, system='default'):
    node_key = 'nv:%s' % node
    return get_redis(system).get(node_key).decode()


def set_node_value(node, value, system='default'):
    node_key = 'nv:%s' % node
    return get_redis(system).set(node_key, value)




