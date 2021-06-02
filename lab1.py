from queue import PriorityQueue
import random


def ucs_weight(from_node, to_node, weights=None):
    return weights.get((from_node, to_node), random.randint(0, 10)) if weights else 1


def ucs(graph, start, end, weights=None):
    frontier = PriorityQueue()
    frontier.put((0, start))  # (priority, node)
    explored = []
    weight_list = []

    while True:

        ucs_w, current_node = frontier.get()
        explored.append(current_node)
        weight_list.append(int(ucs_w))

        if current_node == end:
            return explored, weight_list

        for node in graph[current_node]:
            if node not in explored:
                frontier.put((
                    ucs_w + ucs_weight(current_node, node, weights),
                    node
                ))


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

    a, w = ucs(adj_list, list(adj_list.keys())[0], "F")
    print("Path: ", a)

    print("Weight: ", sum(w))
