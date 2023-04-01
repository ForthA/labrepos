def input_data_greedy():
    node1, node2 = input().split()
    nodes = {}
    while True:
        try:
            line = input()
            temp_node1, temp_node2, temp = line.split()
            weight = float(temp)
            if not nodes.get(temp_node1):
                nodes[temp_node1] = []
            nodes[temp_node1].append([temp_node2, weight])

        except (ValueError, EOFError):
            break
    path = path_finding(node1, node2, nodes)
    print(''.join(path))


def path_finding(node1, node2, nodes):
    path = node1
    curr = node1
    while curr != node2:
        if curr not in nodes.keys():
            path = path[:-1]
            curr = path[-1]
        next_w, next_node = -1, -1
        for i in range(len(nodes)):
            if nodes[curr]:
                next_node, next_w = nodes[curr][0][0], nodes[curr][0][1]
            else:
                del nodes[curr]
                path = path[:-1]
                curr = path[-1]
        if next_w == -1 and next_node == -1:
            return "No path"
        for node in nodes[curr]:
            if node[1] <= next_w:
                if node[1] == next_w and node[0] > next_node:
                    continue
                next_node, next_w = node[0], node[1]
        nodes[curr].remove([next_node, next_w])
        curr = next_node
        path += curr
    return path
