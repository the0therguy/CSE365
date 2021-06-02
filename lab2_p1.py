def dfs_limit(graph, start, goal, limit):
    if start == goal:
        return True

    if limit <= 0:
        return False

    for i in graph[start]:
        if dfs_limit(graph, i, goal, limit - 1):
            return True
    return False


if __name__ == '__main__':
    adj_list = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["B", "F"],
        "D": [],
        "E": ["F"],
        "F": []
    }
    if dfs_limit(adj_list, "A", "E", 1):
        print("Goal node is reachable from source")
    else:
        print("not reachable")
