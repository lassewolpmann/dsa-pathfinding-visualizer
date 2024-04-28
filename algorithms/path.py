def trace_back_path(start_pos, end_pos, prev_nodes):
    path = []
    node = end_pos

    while node != start_pos:
        path.append(node)
        node = prev_nodes[node]

    path.append(start_pos)

    path.reverse()

    return path
