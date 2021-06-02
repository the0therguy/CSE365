def dfs_limit(graph, start, goal, limit):
    if start == goal:
        return True

    if limit <= 0:
        return False

    for i in graph[start]:
        if dfs_limit(graph, i, goal, limit - 1):
            return True
    return False


def iterative_dfs(graph, start, goal):
    n = len(graph)

    for i in range(n):
        if dfs_limit(graph, start, goal, i):
            return i + 1


if __name__ == '__main__':
    adj_list = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["B", "F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    if dfs_limit(adj_list, "A", "E", 5):
        print("Goal node is reachable from source")
    else:
        print("not reachable")

    print("Node found in level: ", iterative_dfs(adj_list, "A", "E"))
