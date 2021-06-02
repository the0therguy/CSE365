def dfs_limit(graph, source):
    path = []
    stack = [source]

    while len(stack) != 0:
        s = stack.pop()

        if s not in path:
            path.append(s)

        if s not in graph:
            continue

        for neighbor in graph[s]:
            stack.append(neighbor)

    return " ".join(path)


if __name__ == '__main__':
    graph = {"A": ["D", "C", "B"],
             "B": ["E"],
             "C": ["G", "F"],
             "D": ["H"],
             "E": ["I"],
             "F": ["J"]}

    print(dfs_limit(graph, "A"))
