def find_min(root):
    if root == None:
        return None

    while root.left != None:
        root = root.left

    return root


def inorder_successor_bst(root, d):
    if root == None:
        return None

    successor = None

    while root != None:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:
            if root.right != None:
                successor = find_min(root.right)
            break
    return successor


arr = [25, 125, 200, 350, 50, 75, 100]
root = create_BST(arr) #assume
all_data = bst_to_list(root) #assume

for d in all_data:
    successor = inorder_successor_bst(root, d)
    i = all_data.index(d)
    expected_val = None
    if i < len(all_data) - 1:
        expected_val = all_data[i + 1]
    if expected_val != None:
        assert expected_val == successor.data
    else:
        assert successor == None

    if successor:
        print("(" + str(d) + ", " + str(successor.data), end=") ")
    else:
        print("(" + str(d), end=", None)")