from MinHeap import MinHeap


def input_data_star():
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
    fin_path = path_finding(node1, node2, nodes)
    print(''.join(fin_path))


def heuristic(a, b):
    return abs(ord(a) - ord(b))


def path_finding(node1, node2, nodes):
    o_set = MinHeap()
    o_set.insert((0, node1))
    back = {}
    g_score, f_score = {node1: 0}, {node1: heuristic(node2, node1)}
    while o_set.size != 0:
        curr = o_set.extract_min()[1]

        if curr == node2:
            path = curr
            while curr in back.keys():
                curr = back[curr]
                path += curr
            return path[::-1]
        if curr in nodes:
            for node in nodes[curr]:
                sum_g_score = g_score[curr] + node[1]
                if node[0] not in g_score or sum_g_score < g_score[node[0]]:
                    back[node[0]] = curr
                    g_score[node[0]] = sum_g_score
                    f_score[node[0]] = sum_g_score + heuristic(node2, node[0])
                    o_set.insert((f_score[node[0]], node[0]))
    return "No path"
