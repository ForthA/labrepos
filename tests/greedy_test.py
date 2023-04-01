from src.greedy import path_finding


def greedy_test():
    assert path_finding('a', 'd', {'a': [['b', 1.0], ['d', 8.0]], 'b': [['c', 1.0]], 'c': [['a', 1.0]]}) == 'abcad'
    node1 = 'a'
    node2 = 'e'
    nodes = {
        'a' : [['b', 7.0], ['c', 3.0]],
        'b' : [['c', 1.0], ['e', 4.0]],
        'c' : [['d', 8.0]]
    }
    assert path_finding(node1, node2, nodes) == 'abe'
    node1 = 'a'
    node2 = 'b'
    nodes = {
        'a' : [['b', 1.0], ['c', 1.0]]
    }
    assert path_finding(node1, node2, nodes) == 'ab'