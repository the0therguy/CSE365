time = 0

adj_list = {
    "A": ["B", "D"],
    "B": ["D"],
    "C": ["A", "E"],
    "D": ["C", "F"],
    "E": ["B"],
    "F": ["C"]
}
color = {}
parent = {}
trav_time = {}
dfs_traversal_output = []
level = {}

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    level[node] = -1
    trav_time[node] = [-1, -1]


def dfs_util(u):
    global time
    end_node = "F"
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1
    if end_node == u:
        print(dfs_traversal_output)

    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)

    color[u] = "B"
    trav_time[u][1] = time
    time += 1


# iterative_dfs("A", "E")
dfs_util("A")
print('output', dfs_traversal_output)
print('parent: child', parent)
print('trav_time:', trav_time)
# print(output)
