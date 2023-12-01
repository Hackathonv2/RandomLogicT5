import sys


def get_weight_node(tree: dict, node: str):
    if not (node in tree.keys()):
        return 1
    else:
        weight = 1
        for module in tree[node]:
            weight += get_weight_node(tree, module)
        return weight


def get_weight_tree(tree: dict):
    rst = list()
    for module in tree.keys():
        rst.append((module, get_weight_node(tree, module) - 1))
    return rst


if __name__ == "__main__":
    lines = [line.strip().split(" ") for line in sys.stdin.readlines()]
    nodes = dict()
    for i in range(1, len(lines)):
        if lines[i][0] in nodes.keys():
            nodes[lines[i][0]].append(lines[i][1])
        else:
            nodes[lines[i][0]] = list(lines[i][1])
    print(nodes)
    weight_nodes = get_weight_tree(nodes)
    max_node = 0
    best_node = None
    for node in weight_nodes:
        if node[1] > max_node:
            best_node, max_node = node[0], node[1]
    print(best_node)
