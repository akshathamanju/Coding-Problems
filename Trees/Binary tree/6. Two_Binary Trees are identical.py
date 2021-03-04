class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None


# function to convert sorted array to a
# balanced BST
# input : sorted array of integers
# output: root node of balanced BST
def sortedArrayToBST(arr):
    if not arr:
        return None

    # find middle
    mid = (len(arr)) // 2

    # make the middle element the root
    root = Node(arr[mid])

    # left subtree of root has all
    # values <arr[mid]
    root.left = sortedArrayToBST(arr[:mid])

    # right subtree of root has all
    # values >arr[mid]
    root.right = sortedArrayToBST(arr[mid + 1:])
    return root
def are_identical(root1, root2):
    if root1 == None and root2 == None:
        return True

    if root1 != None and root2 != None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    return False


arr1 = [100, 50, 200, 25, 125, 350]
arr2 = [1, 2, 10, 50, 180, 199]
arr1.sort()
arr2.sort()
root1 = sortedArrayToBST(arr1)
root2 = sortedArrayToBST(arr2)

arr3 = [100, 50, 200, 25, 125, 350]
arr4 = [100, 50, 200, 25, 125, 350]
arr3.sort()
arr4.sort()
root3= sortedArrayToBST(arr3)
root4 = sortedArrayToBST(arr4)

if (are_identical(root1, root2)):
    print("The trees are identical")
else:
    print("The trees are not identical")


if (are_identical(root3, root4)):
    print("The trees are identical")
else:
    print("The trees are not identical")