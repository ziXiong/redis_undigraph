from redis_undigraph import *


def test_edges():
    #test add edge
    add_edge('girl', 'boy1')
    assert has_edge('girl', 'boy1') is True
    assert has_edge('boy1', 'girl') is True

    #test neighbors
    add_edge('girl', 'boy2')
    neighborlist = neighbors('girl')
    assert 'boy1' in neighborlist
    assert 'boy2' in neighborlist
    assert len(neighborlist) == 2

    #test deleting edge
    delete_edge('girl', 'boy2')
    assert has_edge('girl', 'boy2') is False
    assert has_edge('boy2', 'girl') is False


def test_edge_value():
    assert get_edge_value('girl', 'boy1') is None
    set_edge_value('girl', 'boy1', value='in love')
    assert get_edge_value('girl', 'boy1') == 'in love'
    assert get_edge_value('boy1', 'girl') == 'in love'


def test_node_value():
    assert get_node_value('girl') is None
    set_node_value('girl', 'beautiful')
    assert get_node_value('girl') == 'beautiful'


def test_delete_node():
    #test deleting node, cleaning up node value and edge value
    delete_node('girl')
    assert get_edge_value('girl', 'boy1') is None
    assert get_node_value('girl') is None


if __name__ == '__main__':
    setup_system(name='default', host='yunserver', port='6379', db=2, password='redispass')
    test_edges()
    test_edge_value()
    test_node_value()
    test_delete_node()
