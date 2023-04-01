from src.a_star import path_finding


def a_star_test():
    assert path_finding('a', 'e', {'a': [['b', 3.0], ['d', 5.0]], 'b': [['c', 1.0]], 'c': [['d', 1.0]], 'd' : [['e', 1.0]]}) == 'ade'
    node1 = 'a'
    node2 = 'e'
    nodes = {
        'a': [['b', 7.0], ['c', 3.0]],
        'b': [['c', 1.0], ['e', 4.0]],
        'c': [['d', 8.0]]
    }
    assert path_finding(node1, node2, nodes) == 'abe'
    node1 = 'a'
    node2 = 'b'
    nodes = {
        'a': [['b', 1.0], ['c', 1.0]]
    }
    assert path_finding(node1, node2, nodes) == 'ab'
