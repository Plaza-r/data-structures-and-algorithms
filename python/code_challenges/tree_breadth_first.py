from data_structures.queue import Queue

def breadth_first(tree):
    search = Queue()
    tree_val = []
    if not tree:
        return tree_val
    if not tree.root:
        return tree_val
    if not search.front:
        search.enqueue(tree.root)

    while search.front:
        root = search.dequeue()
        tree_val.append(root.value)
        if root.left:
            search.enqueue(root.left)
        if root.right:
            search.enqueue(root.right)

    return (tree_val)
