from queue import Queue


def dfs(graph, start, goal):
    visited = {}
    level = {}
    parent = {}
    bfs_traversal_output = []
    queue = Queue()

    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    s = start
    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():
        u = queue.get()
        bfs_traversal_output.append(u)

        if u == goal:
            return bfs_traversal_output

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)


if __name__ == '__main__':
    adj_list = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["B"],
        "D": ["A", "E", "F"],
        "E": ["D", "F", "G"],
        "F": ["D", "E", "H"],
        "G": ["E", "H"],
        "H": ["G", "F"]
    }

    a = dfs(adj_list, list(adj_list.keys())[0], "C")
    print(a)
